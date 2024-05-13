from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from moviepy.editor import *
from bs4 import BeautifulSoup
import shutil




def get_path():
    path=filedialog.askdirectory()
    path_label.config(text=path)

def download():
    video_path=url_entry.get()
    file_path=path_label.cget("text")
    print("Downloading.....")

    # Create a YouTube object
    yt = YouTube(video_path)

    # Get the highest resolution stream
    mp4 = yt.streams.get_highest_resolution().download()

    # Download the video
    video_clip = VideoFileClip(mp4) 



    

    #code for mp3
    audio_file=video_clip.audio
    audio_file.write_audiofile('audio2.mp3')
    audio_file.close()
    shutil.move('audio2.mp3',file_path)
    #code for mp3
    
    video_clip.close()
    shutil.move(mp4,file_path)
    print("Download Complete")


root=Tk()

root.title("Video Downloader")
canvas=Canvas(root,width=400,height=300)
canvas.pack()

#app label
app_label=Label(root,text="Video Downloader",fg='blue',font=('Arial',20))
canvas.create_window(200,20,window=app_label)

# Entry to accept video url
url_label=Label(root,text="Enter video URL")
url_entry=Entry(root)
canvas.create_window(200,80,window=url_label)
canvas.create_window(200,100,window=url_entry)

#path to download videos
path_label=Label(root,text="Select Path to download",)
path_button=Button(root,text="Select",command=get_path)
canvas.create_window(200,150,window=path_label)
canvas.create_window(200,170,window=path_button)

#download button
download_button=Button(root,text="Download",command=download)
canvas.create_window(200,250,window=download_button)



root.mainloop()