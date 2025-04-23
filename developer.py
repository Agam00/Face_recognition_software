from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Developer")

        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",32,"bold"),bg="white",fg="blue")
        title_lbl.place(x=0,y=0,width=1360,height=35)
#==========top image=============

        img_top = Image.open(r"img\dev.jpg")
        img_top = img_top.resize((1360,720), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoimg_top)
        f_lbl.place(x=0, y=40, width=1360, height=720)

#frame
        main_frame=Frame(f_lbl,bd=2,bg="white")
        main_frame.place(x=860,y=0,width=500,height=600)

        img_top1 = Image.open(r"img\developers.jpg")
        img_top1 = img_top1.resize((300,200), Image.ANTIALIAS)
        self.photoimg_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoimg_top1)
        f_lbl.place(x=230, y=0, width=300, height=200)

    #Developer info======
        dev_label=Label(main_frame,text="Hello! this is our project",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="We both have created",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=40)

        dev_label=Label(main_frame,text="this python project",font=("times new roman",15,"bold"),bg="white")
        dev_label.place(x=0,y=75)
#bottom image
        img_top2 = Image.open(r"img\imagedev.jpg")
        img_top2 = img_top2.resize((480,380), Image.ANTIALIAS)
        self.photoimg_top2 = ImageTk.PhotoImage(img_top2)

        f_lbl = Label(main_frame, image=self.photoimg_top2)
        f_lbl.place(x=8, y=210, width=480, height=380)






if __name__ =="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()