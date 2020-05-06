from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import sys


def loadWeight(pixels,path):

    
    pre_trained_model = InceptionV3(
        input_shape=(pixels, pixels, 1), include_top=False, weights=None)
    pre_trained_model.load_weights(local_weights_file)

  
    last_layer = pre_trained_model.get_layer('mixed7')
    last_output = last_layer.output

    return last_output, pre_trained_model

def configureLayers(last_output, pre_trained_model):

    
    x = layers.Flatten()(last_output)
    # Add a classifer layers:1,024 hidden units and ReLU activation
    x = layers.Dense(1024, activation='relu')(x)
    x = layers.Dropout(0.2)(x)
    x = layers.Dense(1, activation='sigmoid')(x)

    model = Model(pre_trained_model.input, x)
    model.compile(loss='binary_crossentropy',
              optimizer=RMSprop(lr=0.0001),
              metrics=['acc'])
    return model

def create_model(pixels,cb):
  last_output, pre_trained_model= loadWeight(pixels,cb)
  return configureLayers(last_output,pre_trained_model)

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
        color_mode='grayscale',
        batch_size=20,
        class_mode='binary')

    valid_generator = val_datagen.flow_from_directory(
        valid_dir,
        target_size=(pixels, pixels),
        color_mode='grayscale',
        batch_size=20,
        class_mode='binary')
  
    return train_generator, valid_generator


def trainModel(model, train_generator, valid_generator, epoch, cppath):
    cp_callback = keras.callbacks.ModelCheckpoint(cppath+"/weights.{epoch:02d}.ckpt",
                                          save_weights_only=True,verbose=1)
    history = model.fit(
        train_generator,
        steps_per_epoch=len(train_generator),
        epochs=1,
        validation_data=valid_generator,
        validation_steps=len(valid_generator),
        callbacks=[cp_callback],
        verbose=2)
    return model




mpath=sys.argv[3]
tpath=sys.argv[1]
vpath=sys.argv[2]


pixel=350


model=create_model(pixel)

train_generator, valid_generator=imgGenerator(tpath,vpath,pixel)

model=trainModel(model,train_generator, valid_generator,50,mpath)









