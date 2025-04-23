from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("student attendance")

        #text variables=======
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
        # first image
        img = Image.open(r"img\smart-attendance.jpg")
        img = img.resize((680,200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=680, height=200)


        # second image
        img1 = Image.open(r"img\lyallpurkhalsa.jpg")
        img1 = img1.resize((680, 200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=680, y=0, width=680, height=200)

         #background image
        img3 = Image.open(r"img\background.png")
        img3 = img3.resize((1366, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=200, width=1366, height=710)

        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",32,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1360,height=35)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=15,y=40,width=1330,height=540)

        #left side lable frame1
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",11,"bold"))
        Left_frame.place(x=10,y=5,width=640,height=538)

        img_left = Image.open(r"img\students-in-classroom.jpg")
        img_left = img_left.resize((625,130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=3, y=0, width=625, height=130)

        left_inside_frame=Frame(Left_frame,bd=2,relief=RIDGE,bg="white")
        left_inside_frame.place(x=3,y=135,width=625,height=280)
        
        #lable and entry=====
        #attendanceID
        AttendanceID_label=Label(left_inside_frame,text="AttendanceID",font=("times new roman",11,"bold"),bg="white")
        AttendanceID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        AttendanceID_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",10,"bold"))
        AttendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #ROLL
        roll_label=Label(left_inside_frame,text="Roll",font=("times new roman",11,"bold"),bg="white")
        roll_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        Atten_entry=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",10,"bold"))
        Atten_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #name
        name_label=Label(left_inside_frame,text="Name",font=("times new roman",11,"bold"),bg="white")
        name_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        Atten_name=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",10,"bold"))
        Atten_name.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #department
        dep_label=Label(left_inside_frame,text="Department",font=("times new roman",11,"bold"),bg="white")
        dep_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        Atten_dep=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",10,"bold"))
        Atten_dep.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #time
        time_label=Label(left_inside_frame,text="Time",font=("times new roman",11,"bold"),bg="white")
        time_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        Atten_time=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",10,"bold"))
        Atten_time.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #date
        date_label=Label(left_inside_frame,text="Date",font=("times new roman",11,"bold"),bg="white")
        date_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        Atten_date=ttk.Entry(left_inside_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",10,"bold"))
        Atten_date.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #attendance
        attendance=Label(left_inside_frame,text="Attendnace Status",bg="white",font=("times new roman",10,"bold"))
        attendance.grid(row=3,column=0)

        self.atten_status=ttk.Combobox(left_inside_frame,width=20,textvariable=self.var_atten_attendance,font=("times new roman",11,"bold"),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.grid(row=3,column=1,pady=8)
        self.atten_status.current(0)

        #buttons frame
        btn_frame=Frame(left_inside_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=240,width=620,height=30) 

        save_btn=Button(btn_frame,text="IMPORT CSV",command=self.importCsv,width=16,font=("Times New Roman",11,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="EXPORT CSV",command=self.exportCsv,width=16,font=("Times New Roman",11,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="UPDATE",width=16,font=("Times New Roman",11,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="RESET",width=16,command=self.reset_data,font=("Times New Roman",11,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        #right side lable frame1
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=655,y=5,width=658,height=580)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="white")
        table_frame.place(x=5,y=5,width=640,height=400)

        #======scrollbar table========
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(table_frame,column=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"

        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
    #===fetch data============
    
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
        self.AttendanceReportTable.insert("",END,values=i)

    #import csv=======
    def importCsv(self):
      global mydata
      mydata.clear()
      fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
      with open(fln) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
        self.fetchData(mydata)

    #export csv========
    def exportCsv(self):
      try:
        if len(mydata)<1:
          messagebox.showerror("No Data","No data found to export",parent=self.root)
          return False
        fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(fln,mode="w",newline="") as myfile:
          exp_write=csv.writer(myfile,delimiter=",")
          for i in mydata:
            exp_write.writerow(i)
          messagebox.showinfo("Data Export","Your Data Exported to"+os.path.basename(fln)+" successfully",parent=self.root)
      except Exception as es:
          messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)
    

    #fetch data in form=======
    
    def get_cursor(self,event=""):
      cursor_row=self.AttendanceReportTable.focus()
      content=self.AttendanceReportTable.item(cursor_row)
      rows=content["values"]
      self.var_atten_id.set(rows[0])
      self.var_atten_roll.set(rows[1])
      self.var_atten_name.set(rows[2])
      self.var_atten_dep.set(rows[3])
      self.var_atten_time.set(rows[4])
      self.var_atten_date.set(rows[5])
      self.var_atten_attendance.set(rows[6])

    #reset data====
    def reset_data(self):
      self.var_atten_id.set("")
      self.var_atten_roll.set("")
      self.var_atten_name.set("")
      self.var_atten_dep.set("")
      self.var_atten_time.set("")
      self.var_atten_date.set("")
      self.var_atten_attendance.set("")







if __name__ =="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()