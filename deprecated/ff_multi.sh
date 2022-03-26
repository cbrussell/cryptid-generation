cd output || exit
mkdir videos
mkdir gifs
cd raw || exit

for i in {501..501}
do
    cd "${i}" || exit
    ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -i "${i}_%03d.png"  -c:v libx264 -crf 8 -pix_fmt yuv420p ../../videos/"${i}".mp4 
    
    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -vf palettegen  ${i}_palette.png

    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -i ${i}_palette.png -filter_complex "[0]scale=800:-1:flags=lanczos[j];[j][1]paletteuse" ../../gifs/"${i}".gif

    rm ${i}_palette.png


#new method
    # ffmpeg -y -thread_queue_size 512 -i ./${i}_%03d.png -vf palettegen=reserve_transparent=1 -f apng pipe:1 \
    # | ffmpeg -framerate 10 -y -thread_queue_size 512 -i ./${i}_%03d.png -thread_queue_size 512 -i - -lavfi paletteuse=alpha_threshold=128 -gifflags -offsetting ../../gifs/"${i}".gif

    # ffmpeg -y -hide_banner -v warning -thread_queue_size 512 -i ../../gifs/"${i}".gif -filter_complex "[0:v] scale=900:-1:flags=lanczos,split [a][b]; [a] palettegen=reserve_transparent=on:transparency_color=ffffff [p]; [b][p] paletteuse" ../../gifs/"${i}_900".gif
   
   
   
    cd ..
    done