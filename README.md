# This is still WIP. You can still test it here! Welcome! 

## Draft sample. STILL TUNING. Currently tested on M2 Mac only. Willing to work with you for windows 11 (i have w8) or linux! 


https://github.com/Kakcalu13/generate_animation/assets/65916520/c4f15a8e-d703-45e6-9f13-948c43b8d938


## Ugly instruction list. Please don't hestiate to open an issue if you happened to find here.
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
