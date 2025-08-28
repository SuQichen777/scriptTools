#!/bin/bash
for f in *.m4a; do
    outName="${f%.m4a}.mp3"
    echo "Converting $f to $outName"
    ffmpeg -y -i "$f" -c:a libmp3lame "$outName"
done
