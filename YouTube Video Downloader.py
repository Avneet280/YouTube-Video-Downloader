from tkinter import *
from pytube import YouTube
root=Tk()
root.geometry("700x400")
root.title("YouTube Video Downloader")
root.config(bg="#FFD8B0")
Label(root,text="Enter your link below",font="arial 25 bold").pack(pady=30)
link=StringVar()
Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2,textvariable=link).pack(pady=10)

def download():
    url=YouTube(str(link.get()))
    video=url.streams.get_highest_resolution()
    video.download()
    Label(root,text="downloaded",font=15).pack(pady=20)

    
Button(root,text="Download",font=("arial",20,"bold"),fg="white",bg="red",command=download).pack(pady=30)

root.mainloop()