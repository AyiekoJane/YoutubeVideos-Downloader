import shutil
from tkinter import *
from tkinter import filedialog
from turtle import Screen
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil



#functions
def select_path():
    #allows user to select path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text = path)

def download_file():
    #get user path
    get_link = link_field.get()

    #get selected path
    user_path = path_label.cget("text")
    Screen.title('Downloading...')

    #download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid = VideoFileClip(mp4_video)
    vid.close()

    #move to selected directory
    shutil.move(mp4_video, user_path)
    Screen.title('Download Complete! Dowbload another File...')


Screen = Tk()
title = Screen.title("YouTube Download")
canvas = Canvas(Screen, width = 500, height = 500)
canvas.pack()

#add logo
logo_img = PhotoImage(file = 'YT.png')

#resize
logo_img = logo_img.subsample(2,2)

canvas.create_image (250, 80, image = logo_img)
#link field

link_field = Entry(Screen, width=50)
link_label = Label(Screen, text = " Enter dowbload link: ", font = ('Arial', 15))

#select path for saving file
path_label = Label(Screen, text = "Select path for download", font = ('Arial', 15))
select_btn = Button(Screen,text = "Select", command=select_path)
#add to window
canvas.create_window(250, 280, window = path_label)
canvas.create_window(250, 330, window = select_btn)


# add widgets to the window
canvas.create_window(250, 170, window = link_label)
canvas.create_window(250, 220, window = link_field)

#download buttons
download_btn = Button(Screen, text = "Download File", command = download_file)
#add to window
canvas.create_window(250, 390, window = download_btn)


Screen.mainloop()