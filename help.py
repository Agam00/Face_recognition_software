from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Help")

        title_lbl=Label(self.root,text="HELP DESK",font=("times new roman",32,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1360,height=35)
#==========top image=============

        img_top = Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        img_top = img_top.resize((1360,720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1360, height=720)

        dev_label=Label(f_lbl,text="Email: kalrakamal1568@gmail.com",font=("times new roman",25,"bold"),bg="white")
        dev_label.place(x=415,y=200)

if __name__ =="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()