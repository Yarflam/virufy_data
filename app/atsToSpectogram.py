import tensorflow_io as tfio
import tensorflow as tf
import sys

# Audio Tensor -> Spectogram
def atsToSpectogram(items, ymax=300):
    output = []
    for item in items:
        sp = tfio.experimental.audio.spectrogram(item, nfft=1024, window=1024, stride=256)
        sp = tfio.experimental.audio.melscale(sp, rate=48000, mels=128, fmin=0, fmax=24000)
        output.append(tf.math.log(sp)[0:ymax])
    return output

sys.modules[__name__] = atsToSpectogram
