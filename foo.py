import tkinter as tk
from tkinter import ttk
import librosa
import pygame
import numpy as np

globalValue = None

def on_slider_change(value):
    # This function is called when the slider value changes
    global globalValue
    globalValue = value
    print("Slider value:", value)
    print("Slider value2:", globalValue)

def on_button_click():
    # This function is called when the button is clicked
    global globalValue
    peaks = librosa.util.peak_pick(onset_env, pre_max=float(globalValue), post_max=float(globalValue), pre_avg=500, post_avg=500, delta=0.02, wait=1)
    peak_times = librosa.frames_to_time(peaks, sr=sr)
    print("GlobalValue = ", globalValue)
    pygame.mixer.music.play()

# Create the main window
root = tk.Tk()
root.title("Slider and Button Frame")


# Create a frame to hold the slider and button
frame = ttk.Frame(root, padding=20)
frame.pack()

# Create a slider
slider_label = ttk.Label(frame, text="Slider:")
slider_label.grid(row=0, column=0, sticky=tk.W)

slider = ttk.Scale(frame, from_=0, to=100, orient=tk.HORIZONTAL, command=on_slider_change)
slider.grid(row=0, column=1, sticky=tk.W)

# Create a button
button = ttk.Button(frame, text="Click Me", command=on_button_click)
button.grid(row=1, columnspan=2)

# create the beat visualizer
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


# Start the main loop
root.mainloop()
