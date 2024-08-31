#!/bin/bash

# Check if no arguments are provided
if [ "$#" -eq 0 ]; then
    echo "Usage: $0 --video | --picture"
    exit 1
fi

if [ "$1" == "--picture" ]; then
    echo "Capturing picture..."
    fswebcam --frames 10 -r 1280x720 --no-banner output.jpg
elif [ "$1" == "--video" ]; then
    echo "Capturing video..."
    ffmpeg -f v4l2 -framerate 30 -video_size 1280x720 -c:v mjpeg -i /dev/video0 -f pulse -i default -t $2 -c:v libx264 output.mov -y
else
    echo "Invalid option. Usage: $0 --video | --picture"
    exit 1
fi