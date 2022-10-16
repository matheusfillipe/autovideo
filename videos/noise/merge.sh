#!/bin/bash

ffmpeg -y -stream_loop -1 -i "$1" -stream_loop -1 -i "$2" -vcodec libx264 -crf 28 -preset faster -tune film -c:a aac -t 60 "$3"
