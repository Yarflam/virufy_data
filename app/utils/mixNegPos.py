import sys

# Mix sets: negative + positive
def mixNegPos(neg, pos):
    output = []
    lneg, lpos = len(neg), len(pos)
    for i in range(0, max(lneg, lpos)):
        if i < lneg: output.append([ neg[i], [1, 0] ])
        if i < lpos: output.append([ pos[i], [0, 1] ])
    return output[::-1]

sys.modules[__name__] = mixNegPos
