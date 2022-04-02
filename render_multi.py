import os
import sys
import subprocess
import shutil
from datetime import datetime

def main():

    start_time = datetime.now()
    frames = 72
    # select files for collage
    files = [20, 8, 13, 18]
 #20
    # frame/file check
    if frames % len(files) != 0:
        sys.exit("Files not divisible into frame count")  

    # generate file string from above
    file_string = ''
    for i in range(len(files)):
        file_string +=  f'_{files[i]}'
    file_string = file_string.strip('_')

    # create unique multi filestring folder for copied frames
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.makedirs(f"{dir_path}/output/multi/{file_string}", exist_ok=True)

    # iterate over incremenet and copy frames
    increment = int(frames / len(files))
    start = 0
    stop = increment

    for i in files:
        print(i)
        for j in range(start, stop):
            print(j)
            raw_frame = f"{dir_path}/output/raw/{i}/{i}_{j:03}.png"
            raw_frame_t = f"{dir_path}/output/raw/{i}/{i}_{j:03}_t.png"
            multi_frame = f"{dir_path}/output/multi/{file_string}/{file_string}_{j:03}.png"
            multi_frame_t = f"{dir_path}/output/multi/{file_string}/{file_string}_{j:03}_t.png"
            shutil.copy(raw_frame, multi_frame)
            shutil.copy(raw_frame_t, multi_frame_t)
        start = stop
        stop += increment

    
    mp4 = f"ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i output/multi/{file_string}/{file_string}_%03d.png  -c:v libx264 -crf 8 -pix_fmt yuv420p output/multi/{file_string}.mp4"
    subprocess.call(mp4,shell=True)
    palette = f' ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/multi/{file_string}/{file_string}_%03d.png -vf "scale=750:-1:flags=lanczos,palettegen=stats_mode=diff" -y output/multi/{file_string}/palette.png'
    subprocess.call(palette,shell=True)
    gif = f'ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/multi/{file_string}/{file_string}_%03d.png -i output/multi/{file_string}/palette.png -filter_complex "scale=750:-1:flags=lanczos,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle"  output/multi/{file_string}.gif'
    subprocess.call(gif,shell=True)
    png = f'ffmpeg -r 24 -y -thread_queue_size 512  -i output/multi/{file_string}/{file_string}_%03d_t.png  -filter_complex "scale=750:-1:flags=lanczos,setpts=PTS-STARTPTS" -plays 0 -f apng output/multi/{file_string}.png'
    subprocess.call(png,shell=True)

    end_time = datetime.now()
    elapsed_time = end_time - start_time
    
    print(f'Completed building multi image {file_string} in {elapsed_time}.')
     
    return
   
if __name__ == '__main__':
    main()