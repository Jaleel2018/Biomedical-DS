# -*- coding: utf-8 -*-
"""
Jaleel Christopher Homework 2 ANN
"""
import numpy as np
import tensorflow as tf
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from tensorflow.keras.optimizers import SGD
import random

#Initialize lists
x1 = []
x2 = []
y1 = []
y2 = []
#Create Data points
for i in range(400):
    x1.append(random.uniform(0,0.5))
    x2.append(random.uniform(0.5,1)) 
    y1.append(random.uniform(0,0.5))
    y2.append(random.uniform(0.5,1))

#Create each set
s1 = pd.DataFrame({"X":x1[:200],"Y":y1[:200],"XOR":[0]*200})
s2 = pd.DataFrame({"X":x1[200:400],"Y":y2[:200],"XOR":[1]*200})
s3 = pd.DataFrame({"X":x2[:200],"Y":y1[200:400],"XOR":[1]*200})
s4 = pd.DataFrame({"X":x2[200:400],"Y":y2[200:400],"XOR":[0]*200})
#Consolidate data into training and testing set
train_set = s1[:100].append(s2[:100],ignore_index = True)
train_set = train_set.append(s3[:100],ignore_index = True)
train_set = train_set.append(s4[:100],ignore_index = True)
test_set = s1[100:200].append(s2[100:200],ignore_index = True)
test_set = test_set.append(s3[100:200],ignore_index = True)
test_set = test_set.append(s4[100:200],ignore_index = True)

#Split data from labels 
x_train = train_set[['X','Y']]
y_train = train_set['XOR']
x_test = test_set[['X','Y']]
y_test = test_set[['XOR']]

# Convert labels into One Hot Encoding
y_train = tf.keras.utils.to_categorical(y_train,2)
y_test = tf.keras.utils.to_categorical(y_test,2)

#Initiate Training and Validation average accuracy list
final_accuracy_list = []
final_val_list = []


#Create for loop to cycle through each set of epochs for 10 iterations
for i in range(50,300,50):
    count = 0
    accuracy_list = []
    val_list = []
    while count<10:
        xor_model = Sequential()
        xor_model.add(Dense(2, activation = 'tanh',input_shape =(2,)))
        xor_model.add(Dense(2, activation = 'softmax'))
        xor_model.compile(loss='categorical_crossentropy',optimizer = 
                          SGD(learning_rate=0.3), metrics = ['accuracy'])
        xor_model = xor_model.fit(x_train, y_train, batch_size = 8, epochs = i, verbose =1, 
                      validation_data=(x_test,y_test))
        accuracy_list.append(max(xor_model.history['accuracy']))
        val_list.append(max(xor_model.history['val_accuracy']))
        count+=1
    final_accuracy_list.append(np.mean(accuracy_list))
    final_val_list.append(np.mean(val_list))



final_accuracy_list3 = []
final_val_list3 = []

for i in range(50,300,50):
    count = 0
    accuracy_list = []
    val_list = []
    while count<10:
        xor_model = Sequential()
        xor_model.add(Dense(3, activation = 'tanh',input_shape =(2,)))
        xor_model.add(Dense(2, activation = 'softmax'))
        xor_model.compile(loss='categorical_crossentropy',optimizer = 
                          SGD(learning_rate=0.3), metrics = ['accuracy'])
        xor_model = xor_model.fit(x_train, y_train, batch_size = 8, epochs = i, verbose =1, 
                      validation_data=(x_test,y_test))
        accuracy_list.append(np.mean(xor_model.history['accuracy']))
        val_list.append(np.mean(xor_model.history['val_accuracy']))
        count+=1
    final_accuracy_list3.append(np.mean(accuracy_list))
    final_val_list3.append(np.mean(val_list))
