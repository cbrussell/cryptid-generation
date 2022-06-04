import os
import subprocess
from datetime import datetime
from multiprocessing import Process, Manager

def main():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.makedirs(f"{dir_path}/output/gifs", exist_ok=True)
    os.makedirs(f"{dir_path}/output/videos", exist_ok=True)
    os.makedirs(f"{dir_path}/output/apngs", exist_ok=True)
    start_time = datetime.now()

    procs = 10  # number of processors
    n = 70 # collection size
    increment = int(n / procs)
    jobs = []
    start = 1
    stop = increment + 1    

    with Manager() as manager:
       
        for i in range(0, procs):
            process = Process(target=worker, args=(start, stop))
            start = stop
            stop += increment
            jobs.append(process)

        [j.start() for j in jobs]
        [j.join() for j in jobs]

        end_time = datetime.now()
        elapsed_time = end_time - start_time
      
        print(f'{n} cryptids generated in {elapsed_time}.')
     
    return

def worker(start, stop):

    for id in range(start, stop):
        number = 0

        mp4 = f"ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i output/raw/{id}/{id}_%03d.png  -c:v libx264 -crf 8 -pix_fmt yuv420p output/videos/{id}.mp4"
        subprocess.call(mp4,shell=True)

        palette = f' ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/raw/{id}/{id}_%03d.png -vf "scale=750:-1:flags=lanczos,palettegen=stats_mode=diff" -y output/raw/{id}/{id}_palette.png'
        subprocess.call(palette,shell=True)

        gif = f'ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/raw/{id}/{id}_%03d.png -i output/raw/{id}/{id}_palette.png -filter_complex "scale=750:-1:flags=lanczos,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle"  output/gifs/{id}.gif'
        subprocess.call(gif,shell=True)

        # png = f'ffmpeg -r 24 -y -thread_queue_size 512  -i output/raw/{id}/{id}_%03d_t.png  -filter_complex "scale=750:-1:flags=lanczos,setpts=PTS-STARTPTS" -plays 0 -f apng output/apngs/{id}.png'
        # subprocess.call(png,shell=True)

        png = f'ffmpeg -r 24 -y -thread_queue_size 512  -i output/raw/{id}/{id}_%03d_t.png  -filter_complex "setpts=PTS-STARTPTS" -plays 0 -f apng output/apngs/{id}.png'
        subprocess.call(png,shell=True)

        number += 1

    print(f'Multiprocess job complete! For process ID {os.getpid()}, {number} cryptids generated.')
   
if __name__ == '__main__':
    main()
