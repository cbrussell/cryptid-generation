import os
import subprocess
from datetime import datetime
from multiprocessing import Process, Manager

def main():

    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.makedirs(f"{dir_path}/output/gifs", exist_ok=True)
    os.makedirs(f"{dir_path}/output/videos", exist_ok=True)
    start_time = datetime.now()

    mp4 = f"ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i output/collage/collage_%03d.png  -c:v libx264 -crf 8 -pix_fmt yuv420p output/videos/collage.mp4"
    subprocess.call(mp4,shell=True)
    palette = f' ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/collage/collage_%03d.png -vf "scale=750:-1:flags=lanczos,palettegen=stats_mode=diff" -y output/collage/collage_palette.png'
    subprocess.call(palette,shell=True)
    gif = f'ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/collage/collage_%03d.png -i output/collage/collage_palette.png -filter_complex "scale=750:-1:flags=lanczos,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle"  output/gifs/collage.gif'
    subprocess.call(gif,shell=True)
    # png = f'ffmpeg -r 24 -y -thread_queue_size 512  -i output/collage/collage_%03d_t.png  -filter_complex "scale=750:-1:flags=lanczos,setpts=PTS-STARTPTS" -plays 0 -f apng output/gifs/collage.png'
    # subprocess.call(png,shell=True)
    

    print(f'Collage render complete')
   
if __name__ == '__main__':
    main()
