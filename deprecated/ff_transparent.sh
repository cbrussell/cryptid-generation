cd output || exit
mkdir videos
mkdir gifs
cd raw || exit

for i in {1..5}
do
    cd "${i}" || exit
    ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i "${i}_%03d.png"  -c:v libx264 -crf 8 -pix_fmt yuv420p ../../videos/"${i}".mp4 
    
    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -vf scale=800x800,palettegen=reserve_transparent=on "${i}_palette.png"

    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -i "${i}_palette.png" -lavfi "[0]scale=800:-1:flags=lanczos[j];[j][1]paletteuse=alpha_threshold=128" -gifflags -offsetting ../../gifs/"${i}".gif

    rm ${i}_palette.png
    
    cd ..
    done