#!/bin/bash

# Python3
sudo apt update && sudo apt install -y python3 python3-pip

# PIP Packages
sudo pip3 install --upgrade pip
sudo pip3 install playsound testresources tensorflow tensorflow-io

# Check CUDA
locate libcudart.so # sudo apt install nvidia-cuda-toolkit
