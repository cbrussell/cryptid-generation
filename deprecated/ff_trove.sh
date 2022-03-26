cd output || exit
mkdir videos
mkdir gifs
cd trove_stills || exit

ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -i "TroveImgSeq_%03d.png"   -c:v libx264 -crf 12  -pix_fmt yuv420p ../videos/TroveImgSeq2.mp4 

#cropping to square
ffmpeg -i ../videos/TroveImgSeq2.mp4 -filter:v "crop=540:540:210:0" ../videos/TroveImgSeq3.mp4

ffmpeg -y -f image2 -framerate 24 -i "TroveImgSeq_%03d.png" -vf scale=960x540,palettegen collage_palette.png

#makes small gif, crop and scale to 95x95
ffmpeg -y -f image2 -framerate 24 -i "TroveImgSeq_%03d.png" -i collage_palette.png -filter_complex "crop=540:540:210:0, scale=540x540[j];[j][1]paletteuse" ../gifs/TroveImgSeq.gif


rm collage_palette.png

