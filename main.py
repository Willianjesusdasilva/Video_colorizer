import numpy as np
from moviepy.editor import *
from abstract_api import colorize_frame
import cv2


def edit_video(video):
    cap = cv2.VideoCapture(video)

    ret, frame = cap.read()
    FPS= cap.get(cv2.CAP_PROP_FPS)
    FrameSize=(frame.shape[1], frame.shape[0])
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')


    out = cv2.VideoWriter('Video_output.mp4', fourcc, FPS, FrameSize)

    while(cap.isOpened()):
        ret, frame = cap.read()
        if not ret: break

        colored = colorize_frame(frame)
        colored = cv2.cvtColor(colored, cv2.COLOR_BGR2RGB)
        out.write(cv2.normalize(colored, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U))


    cap.release()
    out.release()
    cv2.destroyAllWindows() 

    videoclip_orig = VideoFileClip(video)
    videoclip_edit = VideoFileClip('Video_output.mp4')
    final = videoclip_edit.set_audio(videoclip_orig.audio)
    final.write_videofile("output_final.mp4",codec= 'mpeg4')

edit_video('vida.mp4')
