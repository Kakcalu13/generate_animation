1) make a video and named it to here.mp4 then put to smile/
2) python3 makepic.py
3) use diff stable
4) go to root then run ./test.sh (folder name)
5) run commands below:
ffmpeg -framerate 25 -i pic%d.jpg -c:v libx264 -pix_fmt yuv420p -crf 23 
output.mp4

ffmpeg -framerate 25 -i pic%d.jpg output.mp4

ffmpeg -framerate 25 -pattern_type  glob -i “*.png” output.mp4

ffmpeg -framerate 25 -i pic%04d.jpg output.mp4

ffmpeg -framerate 25 -pattern_type  glob -i "filename-*.jpg" output.mp4

ffmpeg -framerate 25 -pattern_type glob -i "filename-*.png" -f lavfi -i 
"aevalsrc=0:d=111.000027" -c:v copy -c:a aac -shortest output.mp4

ffmpeg -framerate 30 -pattern_type glob -i "filename-*.png" -f lavfi -i 
"aevalsrc=0:d=111.000027" -c:v copy -c:a aac -shortest output.mp4
