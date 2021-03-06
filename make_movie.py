import os
from argparse import ArgumentParser
import moviepy.video.io.ImageSequenceClip

fps=3

parser = ArgumentParser()

parser.add_argument('--F', help='The name of the file you want to create images from ', default="image_data")
parser.add_argument('--FPS', help='Frames per second for video ', default=3, type=int)
parser.add_argument('--NUM', help='Frames included in the video ', default=-1, type=int)
args = parser.parse_args()

image_folder=args.F
fps = args.FPS


image_files = [image_folder+'/'+img for img in os.listdir(image_folder) if img.endswith(".png")]
image_files.sort()
if args.NUM > 0:
	image_files = image_files[:args.NUM+1]
clip = moviepy.video.io.ImageSequenceClip.ImageSequenceClip(image_files, fps=fps)
clip.write_videofile('night_sky.mp4')