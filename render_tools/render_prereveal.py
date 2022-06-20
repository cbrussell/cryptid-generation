import os
import subprocess
from datetime import datetime
from multiprocessing import Process, Manager

def main():
       
    mp4 = f"ffmpeg -y -r 24 -start_number 0 -stream_loop 1 -thread_queue_size 512 -i output/prereveal_frames/CryptidsPreview_%03d.png  -c:v libx264 -crf 8 -pix_fmt yuv420p output/prereveal_video.mp4"
    subprocess.call(mp4,shell=True)
    palette = f' ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/prereveal_frames/CryptidsPreview_%03d.png -vf "scale=750:-1:flags=lanczos,palettegen=stats_mode=diff" -y output/prereveal_frames/prereveal_palette.png'
    subprocess.call(palette,shell=True)
    gif = f'ffmpeg -y -f image2 -framerate 24 -thread_queue_size 512 -i output/prereveal_frames/CryptidsPreview_%03d.png -i output/prereveal_frames/prereveal_palette.png -filter_complex "scale=750:-1:flags=lanczos,paletteuse=dither=bayer:bayer_scale=5:diff_mode=rectangle"  output/prereveal_gif.gif'
    subprocess.call(gif,shell=True)
    png = f'ffmpeg -r 24 -y -thread_queue_size 512  -i output/prereveal_frames/CryptidsPreview_%03d.png  -filter_complex "setpts=PTS-STARTPTS" -plays 0 -f apng output/prereveal_apng.png'
    subprocess.call(png,shell=True)
    
    print('Done.')
   
if __name__ == '__main__':
    main()
