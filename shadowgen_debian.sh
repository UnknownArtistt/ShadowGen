#!/bin/bash

# Verify if pip3 is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Installing pip3..."
    sudo apt-get update
    sudo apt-get install python3-pip -y
fi

# Instaling the necessary python modules
echo "Instaling the python modules..."
pip3 install pyfiglet colorama

# Verify if the python script is in the current directory
if [ ! -f "shadowgen.py" ]; then
    echo "Pyhton script not found on the current directory"
    exit 1
fi

# Executing python script
echo "Executing ShadowGen..."
python3 shadowgen.py
