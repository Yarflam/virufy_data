#!/bin/python3
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM
from tensorflow.keras.optimizers import Adam
import matplotlib.pyplot as plt
import numpy as np
import random

from utils import getDataset, getAudioTensors # Dataset tools
from utils import mixNegPos, getDtTVS, getDtXY # Serie tools
import atsToSpectogram

spgm_ymax = 150
serie_ratio = 0.8

# Load dataset
neg, pos = getDataset(True) # (1) Get the files
neg = atsToSpectogram(getAudioTensors(neg), spgm_ymax) # (2) Get Spectogram of Audio Tensor
pos = atsToSpectogram(getAudioTensors(pos), spgm_ymax)
dataset = mixNegPos(neg, pos) # (3) Mix negative and positive
serie_training, serie_validation = getDtTVS(dataset, serie_ratio) # (4) Extract training & validation sets
random.shuffle(serie_training) # (5) Randomize
random.shuffle(serie_validation)
x_train, y_train = getDtXY(serie_training) # (6) Extract (X,Y)
x_valid, y_valid = getDtXY(serie_validation)

print('Training set:  ', x_train.shape)
print('Validation set:', x_valid.shape)

# LSTM Model
model = Sequential()

model.add(LSTM(128, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(128, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(2, activation='softmax'))

opt = Adam(lr=1e-3, decay=1e-5)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])

model.fit(x_train, y_train, epochs=10, validation_data=(x_valid, y_valid))

# Test
predictions = model.predict(x_valid)
lpredict = len(predictions)
for i in range(0, lpredict):
    predict_np = 0 if predictions[i][0] > predictions[i][1] else 1
    good_np = 0 if y_valid[i][0] > y_valid[i][1] else 1
    test_np = '\tWRONG' if not predict_np == good_np else ''
    print('%s\tpredict: %s ; good: %s %s' % (i, predict_np, good_np, test_np))
