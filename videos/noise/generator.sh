#!/bin/bash

# ./this audio_algorithm color output

audio="/tmp/tmp_gen_audio.wav"
video="/tmp/tmp_gen_video.mp4"

./audionoise.sh "$audio" "$1" 1
./colornoise.sh "$2" "$video"
./merge.sh "$video" "$audio" "$3"

rm "$audio"
rm "$video"
