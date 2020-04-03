from tensorflow import keras 
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import sys


#print(sys.argv[1])

mpath=sys.argv[2]
fpath=sys.argv[1]
pixel=350

test_datagen=ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_generator=test_datagen.flow_from_directory(
    fpath,
    target_size=(pixel,pixel),
    batch_size=1,
    class_mode='binary')



names=test_generator.filenames
model=keras.models.load_model(mpath)

result=[]
for i in range(len(names)):
    model.predict(test_generator[i][0])
    result.append(model.predict(test_generator[i][0]))

for i in range(len(names)):
    print(names[i], result[i][0])



