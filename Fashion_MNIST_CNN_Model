"""
Created on Wed Mar  9 20:28:58 2022

@author: jaleelchristopher
"""

import keras
from keras.datasets import fashion_mnist
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import display
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import SGD




(x_Train, y_Train), (x_Test, y_Test) = fashion_mnist.load_data()

print(x_Train.shape)
print(x_Train.max())

#reshape data into 2 dimensions
x_Train = x_Train.reshape(60000, 784)
x_Test = x_Test.reshape(10000, 784)
x_Train = x_Train.astype('float32')/255
x_Test = x_Test.astype('float32')/255
x_train = x_Train
x_test = x_Test
y_test = y_Test
y_train = y_Train
#normalize the value of every pixel into the range of 0 to 1
print(x_train.shape[0], 'training samples')
print(x_test.shape[0], 'test samples')
x_train.shape



fig, ax = plt.subplots(figsize=(3, 3))
for n in range(0, 20,1):
    xtrain=x_train[n,:].reshape(28,28)
    ax.imshow(xtrain, cmap='gray')  
    ax.set_title('label: ' + str(int(y_train[n])), fontsize=16)  
    ax.axis('off')
    plt.draw()
    display.clear_output(wait=True)
    display.display(fig)
    plt.pause(0.1)  
    
neurons = [64,96,128,256]
train_accuracy1 = []
val_accuracy1 = []

for i in neurons:
    fashion_model = Sequential()
    fashion_model.add(Dense(256, activation = 'tanh', input_shape = (784,)))
    fashion_model.add(Dense(i, activation = 'tanh'))
    fashion_model.add(Dense(10, activation='softmax'))
    
    fashion_model.compile(loss = 'sparse_categorical_crossentropy',
                          optimizer = SGD(learning_rate = 0.3), metrics = ['accuracy'])
    fashion_model = fashion_model.fit(x_train, y_train, batch_size = 125, epochs = 25, verbose = 1,
                      validation_data = (x_test,y_test))
    train_accuracy1.append(fashion_model.history['accuracy'][len(fashion_model.history['accuracy'])-1])
    val_accuracy1.append(fashion_model.history['val_accuracy'][len(fashion_model.history['val_accuracy'])-1])

relu_train_accuracy1 = []
relu_val_accuracy1 = []

for i in neurons:
    fashion_model = Sequential()
    fashion_model.add(Dense(256, activation = 'relu', input_shape = (784,)))
    fashion_model.add(Dense(i, activation = 'relu'))
    fashion_model.add(Dense(10, activation='softmax'))
    
    fashion_model.compile(loss = 'sparse_categorical_crossentropy',
                          optimizer = SGD(learning_rate = 0.3), metrics = ['accuracy'])
    fashion_model = fashion_model.fit(x_train, y_train, batch_size = 125, epochs = 25, verbose = 1,
                      validation_data = (x_test,y_test))
    relu_train_accuracy1.append(fashion_model.history['accuracy'][len(fashion_model.history['accuracy'])-1])
    relu_val_accuracy1.append(fashion_model.history['val_accuracy'][len(fashion_model.history['val_accuracy'])-1])


train_accuracy2 = []
val_accuracy2 = []

for i in neurons:
    fashion_model = Sequential()
    fashion_model.add(Dense(i, activation = 'tanh', input_shape = (784,)))
    fashion_model.add(Dense(256, activation = 'tanh'))
    fashion_model.add(Dense(10, activation='softmax'))
    
    fashion_model.compile(loss = 'sparse_categorical_crossentropy',
                          optimizer = SGD(learning_rate = 0.3), metrics = ['accuracy'])
    fashion_model = fashion_model.fit(x_train, y_train, batch_size = 125, epochs = 25, verbose = 1,
                      validation_data = (x_test,y_test))
    train_accuracy2.append(fashion_model.history['accuracy'][len(fashion_model.history['accuracy'])-1])
    val_accuracy2.append(fashion_model.history['val_accuracy'][len(fashion_model.history['val_accuracy'])-1])

relu_train_accuracy2 = []
relu_val_accuracy2 = []

for i in neurons:
    fashion_model = Sequential()
    fashion_model.add(Dense(i, activation = 'relu', input_shape = (784,)))
    fashion_model.add(Dense(256, activation = 'relu'))
    fashion_model.add(Dense(10, activation='softmax'))
    
    fashion_model.compile(loss = 'sparse_categorical_crossentropy',
                          optimizer = SGD(learning_rate = 0.3), metrics = ['accuracy'])
    fashion_model = fashion_model.fit(x_train, y_train, batch_size = 125, epochs = 25, verbose = 1,
                      validation_data = (x_test,y_test))
    relu_train_accuracy2.append(fashion_model.history['accuracy'][len(fashion_model.history['accuracy'])-1])
    relu_val_accuracy2.append(fashion_model.history['val_accuracy'][len(fashion_model.history['val_accuracy'])-1])

ans = pd.DataFrame([train_accuracy1,val_accuracy1,relu_train_accuracy1,
                    relu_val_accuracy1,train_accuracy2,val_accuracy2,
                    relu_train_accuracy2,relu_val_accuracy2], 
                   columns = ['64','96','125','256'],index = ['train_accuracy1','val_accuracy1','relu_train_accuracy1',
                    'relu_val_accuracy1','train_accuracy2','val_accuracy2',
                    'relu_train_accuracy2','relu_val_accuracy2'])
print(ans)



  

    
