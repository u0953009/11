from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import sys


def loadWeight(pixels,path):

    #local_weights_file = r'data/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
    local_weights_file=path
    
    pre_trained_model = InceptionV3(
        input_shape=(pixels, pixels, 3), include_top=False, weights=None)
    pre_trained_model.load_weights(local_weights_file)

    for layer in pre_trained_model.layers:
        layer.trainable = False
  
    last_layer = pre_trained_model.get_layer('mixed7')
    #print('last layer output shape:', last_layer.output_shape)
    last_output = last_layer.output

    return last_output, pre_trained_model

def configureLayers(last_output, pre_trained_model):

    # Flatten the output layer to 1 dimension
    x = layers.Flatten()(last_output)
    # Add a fully connected layer with 1,024 hidden units and ReLU activation
    x = layers.Dense(1024, activation='relu')(x)
    # Add a dropout rate of 0.2
    x = layers.Dropout(0.2)(x)
    # Add a final sigmoid layer for classification
    x = layers.Dense(1, activation='sigmoid')(x)

    model = Model(pre_trained_model.input, x)
    model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.0001),
              metrics=['acc'])
    return model


def imgGenerator(trainpath, validpath, pixels):
    train_dir = trainpath
    valid_dir=validpath

    val_datagen = ImageDataGenerator(rescale=1./255)

    # Add data-augmentation parameters to ImageDataGenerator
    train_datagen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=40,
        width_shift_range=0.2,
        height_shift_range=0.2,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)


    train_generator=train_datagen.flow_from_directory(
        train_dir,
        target_size=(pixels,pixels),
        batch_size=20,
        class_mode='binary')

    valid_generator = val_datagen.flow_from_directory(
        valid_dir,
        target_size=(pixels, pixels),  
        batch_size=20,
        class_mode='binary')
  
    return train_generator, valid_generator


def trainModel(model, train_generator, valid_generator):
    history = model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        epochs=1,
        validation_data=valid_generator,
        validation_steps=len(valid_generator),
        verbose=2)
    return model


mname=sys.argv[3]
tpath=sys.argv[1]
vpath=sys.argv[2]
v3path=r'v3/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5'
pixel=350


last_output, pre_trained_model=loadWeight(pixel, v3path)
model=configureLayers(last_output, pre_trained_model)
train_generator, valid_generator=imgGenerator(tpath,vpath,pixel)

model=trainModel(model,train_generator, valid_generator)

modelpath='models/'+mname
model.save(modelpath)






