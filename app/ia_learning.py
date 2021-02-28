#!/bin/python3
import matplotlib.pyplot as plt
import tensorflow_io as tfio
import tensorflow as tf
import numpy as np
import random

from utils import getDataset, getAudioTensors, mixNegPos, getDtTVS
import atsToSpectogram

# Application
if __name__ == "__main__":
    spcYmax = 150
    tvsRatio = 0.8
    # Load dataset
    neg, pos = getDataset(True) # (1) Get the files
    neg = atsToSpectogram(getAudioTensors(neg), spcYmax) # (2) Get Spectogram of Audio Tensor
    pos = atsToSpectogram(getAudioTensors(pos), spcYmax)
    dataset = mixNegPos(neg, pos) # (3) Mix negative and positive
    sTrain, sValid = getDtTVS(dataset, tvsRatio) # (4) Extract training & validation sets
    random.shuffle(sTrain) # (4) Randomize
    random.shuffle(sValid)
    # Model
    print(sTrain[0][0].shape)
    quit()
    # layer = tf.keras.layers.MultiHeadAttention(num_heads=2, key_dim=2)
    # equation = tf.train.AdamOptimizer(0.01).minimize(ff)
    # Learning
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        #
