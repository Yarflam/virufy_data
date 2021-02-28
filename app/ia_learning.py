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

serie_ratio = 0.8

# Load dataset
neg, pos = getDataset(True) # (1) Get the files
neg = atsToSpectogram(getAudioTensors(neg)) # (2) Get Spectogram of Audio Tensor
pos = atsToSpectogram(getAudioTensors(pos))
dataset = mixNegPos(neg, pos) # (3) Mix negative and positive
serie_training, serie_validation = getDtTVS(dataset, serie_ratio) # (4) Extract training & validation sets
random.shuffle(serie_training) # (5) Randomize
random.shuffle(serie_validation)
x_train, y_train = getDtXY(serie_training) # (6) Extract (X,Y)
x_valid, y_valid = getDtXY(serie_validation)

# Normalize
norm_min = min(np.amin(x_train[np.isfinite(x_train)]), np.amin(x_valid[np.isfinite(x_valid)])) # Start with 0
# x_train[~np.isfinite(x_train)] = norm_min
# x_valid[~np.isfinite(x_valid)] = norm_min
x_train -= norm_min
x_valid -= norm_min
norm_max = max(np.amax(x_train), np.amax(x_valid)) # Force interval [0;1]
x_train /= norm_max if not norm_max == 0 else 1
x_valid /= norm_max if not norm_max == 0 else 1

print('Training set:  ', x_train.shape)
print('Validation set:', x_valid.shape)
print('Min: %s, Max: %s' % ( min(np.amin(x_train),np.amin(x_valid)), min(np.amax(x_train),np.amax(x_valid)) ))

# LSTM Model
model = Sequential()

model.add(LSTM(64, input_shape=(x_train.shape[1:]), activation='relu', return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(64, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(32, activation='relu'))
model.add(Dropout(0.2))

model.add(Dense(2, activation='softmax'))

opt = Adam(lr=1e-3, decay=1e-5)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=100, validation_data=(x_valid, y_valid))

# Graph loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

# Test
predictions = model.predict(x_valid)
lpredict = len(predictions)
for i in range(0, lpredict):
    predict_np = 0 if predictions[i][0] > predictions[i][1] else 1
    predict_diff = abs(predictions[i][0] - predictions[i][1])
    good_np = 0 if y_valid[i][0] > y_valid[i][1] else 1
    test_np = '\tWRONG' if not predict_np == good_np else ''
    print('%s\tpredict: %s ; good: %s ; diff: %s %s' % (i, predict_np, good_np, predict_diff, test_np))
