import librosa
import tkinter as tk
import pygame
import time
import numpy as np

root = tk.Tk()
canvas = tk.Canvas(root, width=200, height=200)
canvas.pack()
x1, y1 = 50, 50  # Top-left corner coordinates
x2, y2 = 150, 150  # Bottom-right corner coordinates
canvas.create_rectangle(x1, y1, x2, y2, fill="white")# Load the audio file

# Initialize pygame and mixer
pygame.init()
pygame.mixer.init()

#audio_file = sys.argv[1]
y, sr = librosa.load('chill.mp3')
audio = pygame.mixer.music.load('chill.mp3')

onset_env = librosa.onset.onset_strength(y=y, sr=sr, hop_length=512, aggregate=np.max)
peaks = librosa.util.peak_pick(onset_env, pre_max=20, post_max=20, pre_avg=500, post_avg=500, delta=0.02, wait=1)
peak_times = librosa.frames_to_time(peaks, sr=sr)

pygame.mixer.music.play()

#i=0
#while pygame.mixer.music.get_busy():
#        current_position = pygame.mixer.music.get_pos() / 1000.0
#        if peak_times[i] <= current_position:
#                canvas.create_rectangle(x1, y1, x2, y2, fill="black")# Load the audio file
#                time.sleep(0.2)
#                i+=1
#        canvas.create_rectangle(x1, y1, x2, y2, fill="white")# Load the audio file
#        foo = pygame.time.wait(100)
#

i=0
while pygame.mixer.music.get_busy():
        current_position = pygame.mixer.music.get_pos() / 1000.0
        if peak_times[i] <= current_position:
                i+=1
                print("boom")

slider = tk.Scale(
    root,
    from_=0,
    to=100,
    orient='vertical',  # horizontal
)
