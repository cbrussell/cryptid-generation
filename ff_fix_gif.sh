cd output || exit
mkdir videos
mkdir gifs
cd raw || exit

for i in {1..30}
do
    cd "${i}" || exit

    # ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -i "${i}_%03d.png"  -c:v libx264 -crf 8 -pix_fmt yuv420p ../../videos/"${i}".mp4 
    
    # ffmpeg -i input.png -vf chromakey=green out.png chromakey=#00b140:0.125:0.0
    
    

    # ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -vf colorkey=0x00b140:0.1:0.1 "${i}_%03d.png"

      ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -filter_complex "chromakey=0x00b140:0.2" -start_number 000 "${i}_%03d-transparent.png"


    #   ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d-transparent.png" -vf  "crop=1050:1050:40:75"  -start_number 000 "${i}_%03d-transparent.png"

    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d-transparent.png" -vf palettegen=reserve_transparent=on:transparency_color=0x00b140  ${i}_palette.png


    # ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d-transparent.png" -i ${i}_palette.png -filter_complex "[0]scale=800:-1:flags=lanczos[j];[j][1]paletteuse"      -gifflags -offsetting  ../../gifs/"${i}".gif

      ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d-transparent.png" -i ${i}_palette.png -filter_complex "[0]scale=800:-1:flags=lanczos[j];[j][1]paletteuse"    -gifflags -offsetting  ../../gifs/"${i}".gif

    # rm ${i}_palette.png

    # -gifflags -offsetting

# new method
#     ffmpeg -y -thread_queue_size 512 -i ./${i}_%03d.png -vf palettegen=reserve_transparent=1 -f apng pipe:1 \
#     | ffmpeg -framerate 10 -y -thread_queue_size 512 -i ./${i}_%03d.png -thread_queue_size 512 -i - -lavfi paletteuse=alpha_threshold=128 -gifflags -offsetting ../../gifs/"${i}".gif

#     ffmpeg -y -hide_banner -v warning -thread_queue_size 512 -i ../../gifs/"${i}".gif -filter_complex "[0:v] scale=900:-1:flags=lanczos,split [a][b]; [a] palettegen=reserve_transparent=on:transparency_color=ffffff [p]; [b][p] paletteuse" ../../gifs/"${i}_900".gif
   
   
    cd ..
    done
