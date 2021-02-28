#!/bin/python3
import matplotlib.pyplot as plt
import tensorflow_io as tfio
import tensorflow as tf
import numpy as np

from utils import getDataset, getAudioTensors

def spectrogram(audio_tensor):
    sp = tfio.experimental.audio.spectrogram(audio_tensor, nfft=1024, window=1024, stride=256)
    return tf.math.log(sp)[0:150]

# Application
if __name__ == "__main__":
    # Load dataset
    neg, pos = getDataset()
    neg = getAudioTensors(neg)
    pos = getAudioTensors(pos)
    # Show
    plt.imshow(spectrogram(pos[0]).numpy())
    plt.show()
