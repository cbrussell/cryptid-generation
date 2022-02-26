cd output || exit
mkdir videos
mkdir gifs
cd raw || exit

for i in {1..20}
do
    cd "${i}" || exit
    ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -i "${i}_%03d.png"  -c:v libx264 -crf 12 -pix_fmt yuv420p ../../videos/"${i}".mp4 
    
    ffmpeg -y -f image2 -framerate 24 -i "${i}_%03d.png" -vf scale=590x590,palettegen ${i}_palette.png

    ffmpeg -y -f image2 -framerate 24 -i "${i}_%03d.png" -i ${i}_palette.png -filter_complex "[0]scale=590x590[j];[j][1]paletteuse" ../../gifs/"${i}".gif

    rm ${i}_palette.png
    
    cd ..
    done