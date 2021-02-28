import tensorflow_io as tfio
import tensorflow as tf
import sys

def getAudioTensors(files):
    output = []
    for file in files:
        audio = tfio.audio.AudioIOTensor(file)
        audio_tensor = audio.to_tensor()
        audio_tensor = tf.squeeze(audio_tensor, axis=[-1])
        audio_tensor._srcAudio = audio
        output.append(audio_tensor)
    return output

sys.modules[__name__] = getAudioTensors
