from tkinter import *                   # tkinter ===> tk interface... tk ante telusu gaa
from pytube import YouTube


## download this video ====> https://www.youtube.com/watch?v=jNQXAC9IVRw
root = Tk()
root.geometry('450x300')
#root.resizable(0, 0)
root.title("video23")  # Title of the program

Label(root, text='video24', font='arial 15 bold').pack()  # Title of the program
link = StringVar()  # Variable for save link of video
filename = StringVar()  # Variable for save link of video

Label(root, text='ikkada link pettuko', font='arial 13 bold').place(x=160, y=40)
link_enter = Entry(root, width=45, textvariable=link).place(x=50, y=90)  # Input for add the link

def Download23():
    Label(root, text='Download autundi aagu', font='arial 13').place(x=180, y=210)
    url = YouTube(str(link.get()))
    video = url.streams.get_highest_resolution()
    video.download()
    Label(root, text='Downloaded ayindi ga', font='arial 15').place(x=180, y=210)

Button(root, text='Download cheskoo', font='arial 15 bold', padx=2, command=Download23).place(x=180, y=150)

root.mainloop()