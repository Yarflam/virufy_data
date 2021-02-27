#!/bin/python3
from utils import getDataset, getAudioTensors
import matplotlib.pyplot as plt
import tensorflow_io as tfio
import tensorflow as tf

def spectrogram(audio_tensor):
    sp = tfio.experimental.audio.spectrogram(audio_tensor, nfft=512, window=512, stride=256)
    return tf.math.log(sp)

# Application
if __name__ == "__main__":
    # Load dataset
    neg, pos = getDataset()
    neg = getAudioTensors(neg)
    pos = getAudioTensors(pos)
    # Show
    fig, axs = plt.subplots(2, 2)
    axs[0, 0].plot(spectrogram(neg[0]))
    axs[0, 1].plot(spectrogram(pos[0])) # n0, p0
    axs[1, 0].plot(spectrogram(neg[1]))
    axs[1, 1].plot(spectrogram(pos[1])) # n1, p1
    plt.show()
