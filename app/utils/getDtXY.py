import numpy as np
import math
import sys

# Extract (X,Y) of training/validation set
def getDtXY(serie):
    x_set, y_set = [], []
    for item in serie:
        x_set.append(item[0])
        y_set.append(item[1])
    return np.array(x_set), np.array(y_set)

sys.modules[__name__] = getDtXY
