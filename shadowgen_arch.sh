#!/bin/bash

# Verify if Python and pip are installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Installing Python3..."
    sudo pacman -Sy python
fi

if ! command -v pip &> /dev/null
then
    echo "pip is not installed. Installing pip..."
    sudo pacman -Sy python-pip
fi

# Installing the necessary Python modules
echo "Installing the Python modules..."
pip install pyfiglet colorama

# Verify if the Python script is in the current directory
if [ ! -f "shadowgen.py" ]; then
    echo "Python script not found in the current directory."
    exit 1
fi

# Executing Python script
echo "Executing ShadowGen..."
python3 shadowgen.py
