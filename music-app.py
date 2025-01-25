import os
from tkinter import *
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Global variable to store the current song path
current_song = None
paused = False

# Function to load a song
def load_song():
    global current_song
    file_path = filedialog.askopenfilename(filetypes=[("Music Files", "*.mp3 *.wav *.mpeg")])
    if file_path:
        current_song = file_path
        song_label.config(text="Loaded: " + os.path.basename(file_path))
        pygame.mixer.music.load(file_path)

# Function to play the loaded song
def play_song():
    global paused
    if current_song:
        pygame.mixer.music.play()
        paused = False
        status_label.config(text="Playing")

# Function to pause the song
def pause_song():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
        status_label.config(text="Paused")

# Function to resume the song
def resume_song():
    global paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
        status_label.config(text="Playing")

# Function to stop the song
def stop_song():
    pygame.mixer.music.stop()
    status_label.config(text="Stopped")

# Initialize the app window
app = Tk()
app.title("Music Player")
app.geometry("400x400")
app.resizable(False, False)

# Title Label
Label(app, text="Music Player", font=("Arial", 16, "bold")).pack(pady=10)

# Song Label
song_label = Label(app, text="No song loaded", wraplength=350, font=("Arial", 12))
song_label.pack(pady=10)

# Status Label
status_label = Label(app, text="Status: Stopped", font=("Arial", 12))
status_label.pack(pady=10)

# Buttons
Button(app, text="Load", command=load_song, width=20, bg="lightblue").pack(pady=5)
Button(app, text="Play", command=play_song, width=20, bg="lightgreen").pack(pady=5)
Button(app, text="Pause", command=pause_song, width=20, bg="yellow").pack(pady=5)
Button(app, text="Resume", command=resume_song, width=20, bg="lightyellow").pack(pady=5)
Button(app, text="Stop", command=stop_song, width=20, bg="red").pack(pady=5)

# Run the app
app.mainloop()
