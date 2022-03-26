cd output || exit
mkdir videos
mkdir gifs
cd raw || exit

for i in {1..30}
do
    cd "${i}" || exit
    ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i "${i}_%03d.png"  -c:v libx264 -crf 8 -pix_fmt yuv420p ../../videos/"${i}".mp4 
    
    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -vf palettegen=reserve_transparent=on ${i}_palette.png

    ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -i ${i}_palette.png -filter_complex "[0]scale=775:-1:flags=lanczos[j];[j][1]paletteuse=new=1"  ../../gifs/"${i}".gif

    ffmpeg -r 24 -y -thread_queue_size 512  -i "${i}_%03d.png"  -filter_complex "scale=750:-1:flags=bicubic,setpts=PTS-STARTPTS" -plays 0   -f  apng   ../../gifs/"${i}".png

    rm ${i}_palette.png
    
    cd ..
    done