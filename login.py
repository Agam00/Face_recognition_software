from re import L
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     #pip install pillow
from tkinter import messagebox
import mysql.connector
import tkinter
from help import Help
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from time import strftime
from datetime import datetime 

def main():
    win=Tk()
    app=Login_window(win)
    win.mainloop()

class Login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1360x768+0+0")
#background image==========
        img3 = Image.open(r"img\background.png")
        img3 = img3.resize((1366, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=0, width=1366, height=710)

        #frame for login form============
        frame=Frame(self.root,bg="black")
        frame.place(x=540,y=150,width=340,height=450)

        #login image===
        img1=Image.open(r"img\logoimg.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimg1,background="black",borderwidth=0)
        lblimg1.place(x=660,y=165,width=100,height=100)

        get_str=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=70,y=110)

        #labels===
        username_lbl=Label(frame,text="USERNAME",font=("times new roman",15,"bold"),fg="white",bg="black")
        username_lbl.place(x=105,y=150)

        self.textuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textuser.place(x=35,y=180,width=275)

        password_lbl=Label(frame,text="PASSWORD",font=("times new roman",15,"bold"),fg="white",bg="black")
        password_lbl.place(x=105,y=220)

        self.textpass=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.textpass.place(x=35,y=250,width=275)

        #icon images============
        img2=Image.open(r"img\user.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimg2,background="black",borderwidth=0)
        lblimg2.place(x=576,y=305,width=25,height=25)

        img4=Image.open(r"img\password.jpg")
        img4=img4.resize((25,25),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        lblimg4=Label(image=self.photoimg4,background="black",borderwidth=0)
        lblimg4.place(x=576,y=375,width=25,height=25)

        #login button===
        loginbtn=Button(frame,command=self.login,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=110,y=290,width=120,height=35)

        #register button====
        regbtn=Button(frame,command=self.register_window,text="NEW USER REGISTER",font=("times new roman",15,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbtn.place(x=30,y=330,width=270)

        #forgot password button====
        loginbtn=Button(frame,command=self.forgot_password_window,text="FORGOT PASSWORD",font=("times new roman",15,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="black",activeforeground="white",activebackground="black")
        loginbtn.place(x=30,y=380,width=270)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.textuser.get()=="" or self.textpass.get()=="":
            messagebox.showerror("Error","All fields required",parent=self.root)
        elif self.textuser.get()=="kapu" and self.textpass.get()=="123":
            messagebox.showinfo("Success","Welcome to our project",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="test")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from register where email=%s and password=%s",(
                                                                                    self.textuser.get(),
                                                                                    self.textpass.get()
                                                                                ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password",parent=self.root)
            else:
                open_main=messagebox.askyesno("Login","Access only Admin",parent=self.root)
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#================reset password=========================
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Please select the security question",parent=self.root2)
        elif self.security_A_entry.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.new_password_entry.get()=="":
            messagebox.showerror("Error","please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="test")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.combo_security_Q.get(),self.security_A_entry.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_password_entry.get(),self.textuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reseted",parent=self.root2)
                self.root2.destroy()


#==================forgot password window==========================
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please enter the email address to reset your password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="test")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("Error","Please enter the valid username",parent=self.root)
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+540+150")

                l=Label(self.root2,text="FOGOT PASSWORD",font=("times new roman",20,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,width=350)

                security_Q=Label(self.root2,text="Select Security Question",font=("times new roman",17,"bold"),fg="black",bg="white")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your birth place","Your bestfriend's name","Your pet name")
                self.combo_security_Q.place(x=50,y=110,width=250,height=30)
                self.combo_security_Q.current(0)        
                
                security_A=Label(self.root2,text="Security Answer",font=("times new roman",17,"bold"),fg="black",bg="white")
                security_A.place(x=50,y=150)

                self.security_A_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.security_A_entry.place(x=50,y=180,width=250,height=30)

                new_password=Label(self.root2,text="Reset password",font=("times new roman",17,"bold"),fg="black",bg="white")
                new_password.place(x=50,y=220)

                self.new_password_entry=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_password_entry.place(x=50,y=250,width=250,height=30)

                btn=Button(self.root2,command=self.reset_pass,text="RESET",font=("times new roman",15,"bold"),fg="white",bg="green")
                btn.place(x=130,y=290)





# register page==================
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1360x768+0+0")

        #variables==========
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()

        #background image======
        img = Image.open(r"img\background.png")
        img = img.resize((1366, 710), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        bg_img = Label(self.root, image=self.photoimg)
        bg_img.place(x=0, y=0, width=1366, height=710)

        #left image======
        img1 = Image.open(r"img\face_detector1.jpg")
        img1 = img1.resize((500, 550), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        bg_img1 = Label(self.root, image=self.photoimg1)
        bg_img1.place(x=50, y=100, width=500, height=550)

        #frame====
        frame=Frame(self.root,bg="white")
        frame.place(x=550,y=100,width=750,height=550)

        #labels for register form===========
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,"bold"),fg="green",bg="white")
        register_lbl.place(x=250,y=20)

        #labels and entry fields==========
        #first name and last name row 1==========
        fname=Label(frame,text="First Name",font=("times new roman",17,"bold"),fg="black",bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250,height=30)
        
        lname=Label(frame,text="Last Name",font=("times new roman",17,"bold"),fg="black",bg="white")
        lname.place(x=400,y=100)

        self.lname_entry=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.lname_entry.place(x=400,y=130,width=250,height=30)

        #contact and email row 2==========
        contact=Label(frame,text="Contact Number",font=("times new roman",17,"bold"),fg="black",bg="white")
        contact.place(x=50,y=170)

        self.contact_entry=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.contact_entry.place(x=50,y=200,width=250,height=30)
        
        email=Label(frame,text="Eamil",font=("times new roman",17,"bold"),fg="black",bg="white")
        email.place(x=400,y=170)

        self.email_entry=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.email_entry.place(x=400,y=200,width=250,height=30)

        #security question and security answer row3==========
        security_Q=Label(frame,text="Select Security Question",font=("times new roman",17,"bold"),fg="black",bg="white")
        security_Q.place(x=50,y=240)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your birth place","Your bestfriend's name","Your pet name")
        self.combo_security_Q.place(x=50,y=270,width=250,height=30)
        self.combo_security_Q.current(0)        
        
        security_A=Label(frame,text="Security Answer",font=("times new roman",17,"bold"),fg="black",bg="white")
        security_A.place(x=400,y=240)

        self.security_A_entry=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15,"bold"))
        self.security_A_entry.place(x=400,y=270,width=250,height=30)

        #password and confirm password row 4==========
        pswd=Label(frame,text="Password",font=("times new roman",17,"bold"),fg="black",bg="white")
        pswd.place(x=50,y=310)

        self.pswd_entry=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.pswd_entry.place(x=50,y=340,width=250,height=30)
        
        confirm_pswd=Label(frame,text="Confirm Password",font=("times new roman",17,"bold"),fg="black",bg="white")
        confirm_pswd.place(x=400,y=310)

        self.confirm_pswd_entry=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.confirm_pswd_entry.place(x=400,y=340,width=250,height=30)

        #check button============
        self.var_check=IntVar()
        checkbutton=Checkbutton(frame,variable=self.var_check,text="I agree the terms & conditions",font=("times new roman",13,"bold"),fg="black",bg="white",onvalue=1,offvalue=0)
        checkbutton.place(x=50,y=380)

        # buttons==============
        regbtn=Button(frame,command=self.register_data,text="REGISTER NOW",font=("times new roman",15,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        regbtn.place(x=50,y=430,width=270)

        login=Button(frame,command=self.return_login,text="LOGIN NOW",font=("times new roman",15,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        login.place(x=400,y=430,width=270)

        #function declaration=============
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select" or self.var_pass.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:
            messagebox.showerror("Error","You need to agree our terms and conditions",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="",database="test")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!= None:
                messagebox.showerror("Error","Someone has already used this email to register please try another email",parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()
                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered successfully",parent=self.root)

    def return_login(self):
        self.root.destroy()

#face recogntion project================

class Face_Recognition_System:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1366x762+0+0")
        self.root.title("Face Recognition System")

#first image
        img= Image.open(r"img\khalsa.jpg")
        img= img.resize((455,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl= Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=455,height=130)
#second image
        img1 = Image.open(r"img\facialrecognition.png")
        img1= img1.resize((455, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=455, y=0, width=455, height=130)
#third image
        img2 = Image.open(r"img\lyallpurkhalsa.jpg")
        img2 = img2.resize((457, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=911, y=0, width=457, height=130)
#background image
        img3 = Image.open(r"img\background.png")
        img3 = img3.resize((1366, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1366, height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1360,height=45)
#time for project==============
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)

        lbl =Label (self.root, font=('times new roman',14,'bold'),background = 'white',foreground='blue')
        lbl.place(x=0,y=0,width=110,height=50)
        time()


#student button
        img4 = Image.open(r"img\student.jpg")
        img4 = img4.resize((220, 200), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=98,y=70,width=220,height=200)

        b1_1= Button(bg_img,text="STUDENT DETAILS",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=98, y=270, width=220, height=40)

#detect face button
        img5 = Image.open(r"img\face_detector1.jpg")
        img5 = img5.resize((220, 200), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_recognition)
        b1.place(x=416,y=70,width=220,height=200)

        b1_1= Button(bg_img,text="FACE DETECTOR",cursor="hand2",command=self.face_recognition,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=416, y=270, width=220, height=40)

#attendance button
        img6 = Image.open(r"img\smart-attendance.jpg")
        img6 = img6.resize((220, 200), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendance)
        b1.place(x=734,y=70,width=220,height=200)

        b1_1 = Button(bg_img,text="ATTENDANCE",cursor="hand2",command=self.attendance,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=734, y=270, width=220, height=40)

#help button
        img7 = Image.open(r"img\help.jpg")
        img7 = img7.resize((220, 200), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help)
        b1.place(x=1052,y=70,width=220,height=200)

        b1_1 = Button(bg_img,text="HELP DESK",cursor="hand2",command=self.help,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1052, y=270, width=220, height=40)


#train face button
        img8 = Image.open(r"img\train.png")
        img8 = img8.resize((220, 200), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,cursor="hand2",command=self.train_data)
        b1.place(x=98,y=330,width=220,height=200)

        b1_1= Button(bg_img,text="TRAIN DATA",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=98, y=530, width=220, height=40)

#photos button
        img9 = Image.open(r"img\photos.jpg")
        img9 = img9.resize((220, 200), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img)
        b1.place(x=416,y=330,width=220,height=200)

        b1_1= Button(bg_img,text="PHOTOS",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=416, y=530, width=220, height=40)

# developer button
        img10 = Image.open(r"img\dev.jpg")
        img10 = img10.resize((220, 200), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer)
        b1.place(x=734,y=330,width=220,height=200)

        b1_1 = Button(bg_img,text="DEVELOPER",cursor="hand2",command=self.developer,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=734, y=530, width=220, height=40)

#exit button
        img11 = Image.open(r"img\exit.jpg")
        img11= img11.resize((220, 200), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
        b1.place(x=1052,y=330,width=220,height=200)

        b1_1 = Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=1052, y=530, width=220, height=40)

#=========function button=========

#PHOTOS BUTTON
     def open_img(self):
         os.startfile("data")
#EXIT BUTTON
     def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition","Are you sure to exit this project",parent=self.root)
        if self.iExit>0:
           self.root.destroy()
        else:
            return
#STUDENT DETAILS BUTTON
     def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
#TRAIN DATA BUTTON
     def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
#FACE RECOGNITION BUTTON
     def face_recognition(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
#ATTENDANCE BUTTON
     def attendance(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
#DEVELOPER BUTTON
     def developer(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
#HELP BUTTON
     def help(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    main()