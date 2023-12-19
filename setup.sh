#!/bin/bash

# Get the directory where the script is located
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Check if 'data' directory does not exist and then create it
if [[ ! -e $DIR/data ]]; then
    mkdir "$DIR/data"
else
    echo "'data' directory already exists."
fi

# Downloading the image file into the 'data' directory
echo "Downloading tire.jpg from Roboflow..."
curl -o "$DIR/data/tire.jpg" https://media.roboflow.com/tire.jpg
# Alternatively, if you prefer wget, you can use:
# wget https://media.roboflow.com/tire.jpg -O "$DIR/data/tire.jpg"

echo "Download complete."