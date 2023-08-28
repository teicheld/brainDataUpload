import tkinter as tk
import librosa
import librosa.display
import numpy as np
import sys

# Load the audio file
audio_file = sys.argv[1]
y, sr = librosa.load(audio_file)

# Calculate beat frames and beat peaks
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
energy = librosa.feature.rms(y=y)
peaks = librosa.util.peak_pick(energy[0], pre_max=20, post_max=20, pre_avg=500, post_avg=500, delta=0.02, wait=1)
peak_times = librosa.frames_to_time(peaks, sr=sr)

# Create a simple GUI using tkinter
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=400)
canvas.pack()

# Create a rectangle for visualization
rectangle = canvas.create_rectangle(0, 0, 0, 0, fill='blue')  # Initially invisible

# Update the rectangle's size and color based on beat frames and peaks
def update_visualization(frame):
    canvas.coords(rectangle, frame, 0, frame + 10, 400)
    if frame in peaks:
        canvas.itemconfig(rectangle, fill='red')
    else:
        canvas.itemconfig(rectangle, fill='blue')
    root.update()

# Function to play audio
def play_audio():
    for frame in range(len(y)):
        update_visualization(frame)
        if frame in beat_frames or frame in peaks:
            # Play a sound when a beat frame or peak occurs
            pass  # You can add audio playback code here
    update_visualization(len(y))  # Reset visualization at the end

# Add a button to start the visualization and audio playback
play_button = tk.Button(root, text="Play Audio with Visualization", command=play_audio)
play_button.pack()

root.mainloop()
