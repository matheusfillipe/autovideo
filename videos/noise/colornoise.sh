#!/bin/bash

# ffmpeg -f lavfi -i nullsrc=s=1280x720 -filter_complex "geq=random(1)*255:128:128" -t 5 "$2"
# ffmpeg -f rawvideo -video_size 1280x720 -pixel_format ruv420p -framerate 30 -i /dev/urandom -ar 48000 -ac 2 -i /dev/urandom -codec:a copy -t 5 -vf hue=s=0 "$1"

ffmpeg -f rawvideo -video_size 1280x720 -pix_fmt gray16be -framerate 30 -i /dev/urandom -f lavfi -i "color=$1:s=1280x720" -filter_complex "blend=shortest=1:all_mode=overlay:all_opacity=0.7" -t 5 "$2"
