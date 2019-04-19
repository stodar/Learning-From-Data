#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:55:38 2019

@author: siddhi
"""

import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import math

features=[]
labels=[]


with open("marks.txt",'r') as f:
    
    for line in f:   
        
        if not line.strip():
            continue
        marks1,marks2,result=line.strip().split(',')
        
        labels.append(int(result))
        features.append([1,float(marks1),float(marks2)])
        
features=np.array(features)
labels=np.array(labels)

print(features.shape,labels.shape)
print(features)
print(labels)

labels[labels == 0] = -1

x_train, x_test, y_train, y_test = train_test_split(features, labels, test_size=0.25)
N = x_train.shape[0]

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
x_train = sc_X.fit_transform(x_train)
x_test = sc_X.transform(x_test)

def sigmoid(x):
    # Activation function used to map any real value between 0 and 1
    return 1 / (1 + np.exp(-x))

weights=np.zeros(3)
learn_rate = 0.001


for i in range(10000):
    grad=0
    for j in range(N):
        grad=grad + (y_train[j]*x_train[j])/(1+np.exp(y_train[j]*np.dot(weights,x_train[j])))
    
    grad= -1/N*grad
    weights=weights-learn_rate*grad
    
y_pred=np.zeros(y_test.shape)    
print(weights)
for i in range(x_test.shape[0]):
    if(sigmoid(np.dot(x_test[i],weights))<0.5):
        y_pred[i]=-1
    else:
        y_pred[i]=1
    
    
print("Correctly predicted labels:", np.sum(y_test == y_pred)) 
