import random
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
print(tf.__version__)

def loadData(path):
   with np.load(path,allow_pickle=True) as data:
      x_train = data['x_train']
      y_train = data['y_train']
      x_test = data['x_test']
      y_test = data['y_test']
   return x_train,y_train,x_test,y_test
   # data = np.load(path,allow_pickle=True)
   # inp = data['input']
   # out = data['output']
   # return inp,out

# CNN Model
def generateModel():
   # define two sets of inputs
   inputA = layers.Input(shape=(28,140,1))
   inputB = layers.Input(shape=(3,))
   # first convolutional layer
   x = layers.Conv2D(32,3,padding='valid',activation='relu')(inputA)
   x = layers.MaxPooling2D(pool_size=(2,2))(x)

   # second convolutional layer
   x = layers.Conv2D(64,3,activation='relu')(x)
   x = layers.MaxPooling2D(pool_size=(2,2))(x)

   # convolutional model
   x = layers.Flatten()(x)
   x = keras.Model(inputs=inputA, outputs=x)

   # fully connected regression
   combined_input = layers.concatenate([x.output,inputB])
   y = layers.Dense(1024,activation='relu')(combined_input)
   y = layers.Dense(64, activation="relu")(y)
   y = layers.Dense(3, activation="relu")(y)
   y = keras.Model(inputs=[inputA,inputB], outputs=y)
   # combine the output of the two branches
   #combined = layers.concatenate([x.output, y.output])
  
   # # combined outputs
   # z = layers.Dense(2, activation="relu")(combined)
   # z = layers.Dense(1, activation="linear")(z)
   # # our model will accept the inputs of the two branches and
   # # then output a single value
   model = keras.Model(inputs=[x.input, y.input], outputs=y)
   return model

path = 'aero_shape_opt\\datasets\\data_file_cnn.npz'
xtrain,ytrain,xtest,ytest = loadData(path)

model = generateModel()

model.compile(optimizer='adam',
   loss='categorical_crossentropy',
   metrics=['accuracy'])

# print model layers
model.summary()            
