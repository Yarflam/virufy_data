#!/bin/bash
cd "`pwd`/`dirname "$0"`"

# Settings
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/cuda-11.2/targets/x86_64-linux/lib
export TF_CPP_MIN_LOG_LEVEL=3

# Execute
cd app
$@
