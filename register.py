from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk     #pip install pillow
from tkinter import messagebox
import mysql.connector


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

        login=Button(frame,text="LOGIN NOW",font=("times new roman",15,"bold"),borderwidth=0,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
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



        




if __name__ =="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()