cd output || exit
mkdir videos
mkdir gifs
cd raw_shifted || exit

for i in {1..10}
do
    cd "${i}" || exit
    ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i "${i}_%03d.png"  -c:v libx264 -crf 8 -pix_fmt yuv420p ../../videos/"${i}".mp4 
    
    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -vf palettegen=reserve_transparent=on ${i}_palette.png

    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -i ${i}_palette.png -filter_complex "[0]scale=800:-1:flags=lanczos[j];[j][1]paletteuse"  ../../gifs/"${i}".gif

    rm ${i}_palette.png
    
    cd ..
    done