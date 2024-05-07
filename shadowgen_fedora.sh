#!/bin/bash

# Verify if pip3 is installed
if ! command -v pip3 &> /dev/null
then
    echo "pip3 is not installed. Installing pip3..."
    sudo dnf install python3-pip -y
fi

# Installing the necessary python modules
echo "Installing the python modules..."
pip3 install pyfiglet colorama

# Verify if the python script is in the current directory
if [ ! -f "shadowgen.py" ]; then
    echo "Python script not found in the current directory."
    exit 1
fi

# Executing the python script
echo "Executing ShadowGen..."
python3 shadowgen.py
