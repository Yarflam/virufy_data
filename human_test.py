#!/bin/python3
from playsound import playsound
from utils import ls
import random
import time

# Human test
def main ():
    # Original Dataset
    dts = "./clinical/original"
    neg = ls("%s/neg" % dts)
    pos = ls("%s/pos" % dts)
    data = neg + pos
    random.shuffle(data)
    # Try to recognize
    print("Let's see if you can tell by ear if the patient has Covid.\n")
    for dfile in data:
        # Listen
        print("Listen")
        playsound(dfile)
        print("The answer is... (3s)")
        time.sleep(3)
        # Answer
        if "/neg/" in dfile:
            print("Negative")
        else:
            print("Positive")
        print("\n")

main()
