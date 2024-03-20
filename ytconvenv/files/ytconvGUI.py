from tkinter import *
from pytube import YouTube
from pathlib import Path

root = Tk()

root.geometry('500x300')
root.resizable(0, 0)
root.title("YouTube Downloader")
Label(root, text="YT Downloader", font="arial 20 bold").pack()

link = StringVar()

Label(root, text="Enter Link:", font="arial 15 bold",justify="center").place(x=160, y=60)
link_enter = Entry(root, width=70, textvariable=link).place(x=32, y=90)


def Downloader():
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download(str(Path.home() / "Downloads"))
    Label(root, text="Thanks for downloading!", font="arial 15", justify="center").place(x=180, y=210)


Button(root, text="Download", font="arial 15 bold", bg='blue', activebackground="red", padx=2, command=Downloader).place(x=180, y=150)
root.mainloop()
