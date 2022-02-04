cd output || exit
mkdir videos
mkdir gifs
cd collage || exit

ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -i "collage_%03d.png"  -c:v libx264 -crf 12 -pix_fmt yuv420p ../videos/collage.mp4 

ffmpeg -y -f image2 -framerate 24 -i "collage_%03d.png" -vf scale=590x590,palettegen collage_palette.png
ffmpeg -y -f image2 -framerate 24 -i "collage_%03d.png" -i collage_palette.png -filter_complex "[0]scale=590x590[j];[j][1]paletteuse" ../gifs/collage.gif
rm collage_palette.png

