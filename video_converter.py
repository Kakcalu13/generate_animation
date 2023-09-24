from moviepy.editor import VideoFileClip

def convert_mp4_to_mov(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip.write_videofile(output_file, codec='prores')
    clip.close()

input_file = 'test1.mp4'
output_file = 'output.mov'

convert_mp4_to_mov(input_file, output_file)
