import tkinter as tk
import pygame
import os



def play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(playlist.get(tk.ACTIVE))
    var.set(playlist.get(tk.ACTIVE))
    pygame.mixer.music.set_volume(VolumeLevel.get())
    pygame.mixer.music.play()


def Exit():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

player = tk.Tk()

os.chdir("Playlist/")
songlist = os.listdir()

player.title("Mp3 Playa")
player.geometry("600x500")

playlist = tk.Listbox(player,highlightcolor="blue",selectmode = tk.SINGLE)
#print(songlist)
for item in songlist:
    pos = 0
    playlist.insert(pos, item)
    pos = pos + 1

B1 = tk.Button(player,width = 5,height = 3, text = "▌▶ (Play)",command=play)
B2 = tk.Button(player,width = 5,height = 3, text = "▌▌ (Pause)",command=pause)
B3 = tk.Button(player,width = 5,height = 3, text = "▶ (Unpause)",command=unpause)
B4 = tk.Button(player,width = 5,height = 3, text = "✖ (Stop)",command=Exit)

VolumeLevel = tk.Scale(player,from_=0.0,to_=1.0, orient = tk.HORIZONTAL, resolution = 0.01)


l1 = tk.LabelFrame(player,text="Song Name")
l1.pack()

var = tk.StringVar()
songttl = tk.Label(player,textvariable=var)
vollable = tk.Label(player,text = "Volume")
songttl.pack(fill="x")
playlist.pack(fill="both",expand = "yes")
vollable.pack()
VolumeLevel.pack(fill="x")
B1.pack(fill="x")
B2.pack(fill="x")
B3.pack(fill="x")
B4.pack(fill="x")

player.mainloop()