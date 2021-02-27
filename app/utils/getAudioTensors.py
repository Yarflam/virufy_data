import tensorflow_io as tfio
import tensorflow as tf
import sys

def getAudioTensors(files):
    output = []
    for file in files:
        audio_tensor = tfio.audio.AudioIOTensor(file).to_tensor()
        output.append(tf.squeeze(audio_tensor, axis=[-1]))
    return output

sys.modules[__name__] = getAudioTensors
