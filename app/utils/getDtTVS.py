import math
import sys

# Extract from Dataset to series: training and validation
def getDtTVS(dataset, part=2/3):
    ldts = len(dataset)
    pdts = math.ceil(ldts * part)
    return dataset[0:pdts], dataset[pdts:]

sys.modules[__name__] = getDtTVS
