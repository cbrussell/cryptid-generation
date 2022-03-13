cd output || exit
mkdir videos
mkdir gifs
cd raw || exit

for i in {1..5}
do
    cd "${i}" || exit
    # ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i "${i}_%03d.png"  -c:v libx264 -crf 8 -pix_fmt yuv420p ../../videos/"${i}".mp4 
    
    # ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -vf scale=800x800,palettegen ${i}_palette.png

    # ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i "${i}_%03d.png" -i ${i}_palette.png -filter_complex "[0]scale=800:-1:flags=lanczos[j];[j][1]paletteuse" ../../gifs/"${i}".apng

    # rm ${i}_palette.png

    # ffmpeg -r 12 -y -thread_queue_size 512 -i ${i}_%03d.png  -plays 0   apng ../../gifs/"${i}".apng
    
    # ffmpeg -y -f image2 -framerate 24  ${i}_%03d.png -plays 0 ../../gifs/"${i}".apng

    ffmpeg -r 24 -y -thread_queue_size 512  -i "${i}_%03d.png"  -filter_complex "setpts=PTS-STARTPTS,scale=320:-1:flags=lanczos" -plays 0   -f  apng   ../../gifs/"${i}".png

    cd ..
    done