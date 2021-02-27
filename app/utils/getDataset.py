from . import ls
import random
import sys

# Prepare Dataset
def getDataset(rnd=False):
    path = "../clinical/segmented"
    neg = ls("%s/neg" % path)
    pos = ls("%s/pos" % path)
    if rnd:
        random.shuffle(neg)
        random.shuffle(pos)
    return neg, pos

sys.modules[__name__] = getDataset
