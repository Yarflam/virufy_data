import sys

# Mix sets: negative + positive
def mixNegPos(neg, pos):
    output = []
    lneg, lpos = len(neg), len(pos)
    for i in range(0, max(lneg, lpos)):
        if i < lneg: output.append([ neg[i], 0 ]) # neg -> [x, y=0]
        if i < lpos: output.append([ pos[i], 1 ]) # pos -> [x, y=1]
    return output[::-1]

sys.modules[__name__] = mixNegPos
