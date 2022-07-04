from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        # variables__________________________________________
        self.attenID = StringVar()
        self.attenName = StringVar()
        self.attenMSSV = StringVar()
        self.attenClass = StringVar()
        self.attenDate = StringVar()
        self.attenTime = StringVar()
        self.attenStatus = StringVar()

        # first image
        img = Image.open("image/attendance1.jpg")
        img = img.resize((800, 200), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=0, width=800, height=200)

        # second image
        img1 = Image.open("image/attendance2.jpg")
        img1 = img1.resize((800, 200), Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoImage1)
        f_lbl.place(x=800, y=0, width=800, height=200)

        # bg image
        img3 = Image.open("image/BgBlue.png")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoImage3)
        bg_img.place(x=0, y=200, width=1530, height=710)

        title_lbl = Label(bg_img, text="ATTENDANCE STUDENTS SYSTEM", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        # Left label frame
        LeftFrame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance",
                               font=("times new roman", 12, "bold"))
        LeftFrame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("image/StudentDetails.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoImage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(LeftFrame, image=self.photoImage_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        left_inside = Frame(LeftFrame, bd=2, relief=RIDGE, bg="white")
        left_inside.place(x=5, y=135, width=720, height=350)


        #Student id
        AttendanceIDLabel = Label(left_inside, text="ID:", font=("times new roman", 13, "bold"), bg="white")
        AttendanceIDLabel.grid(row=0, column=0, padx=10, pady=8, sticky=W)
        AttendanceIDEntry = ttk.Entry(left_inside, textvariable=self.attenID, width=20, font=("times new roman", 13, "bold"))
        AttendanceIDEntry.grid(row=0, column=1, padx=10, pady=8, sticky=W)

        # Student MSSV
        mssvLabel = Label(left_inside, text="MSSV:", font=("times new roman", 13, "bold"), bg="white")
        mssvLabel.grid(row=0, column=2, padx=10, pady=8, sticky=W)
        mssvEntry = ttk.Entry(left_inside, textvariable=self.attenMSSV, width=20, font=("times new roman", 13, "bold"))
        mssvEntry.grid(row=0, column=3, padx=10, pady=8, sticky=W)

        # Student name
        NameLabel = Label(left_inside, text="Name:", font=("times new roman", 13, "bold"), bg="white")
        NameLabel.grid(row=1, column=0, padx=10, pady=8, sticky=W)
        NameEntry = ttk.Entry(left_inside, textvariable=self.attenName, width=20, font=("times new roman", 13, "bold"))
        NameEntry.grid(row=1, column=1, padx=10, pady=8, sticky=W)

        # Student class
        ClassLabel = Label(left_inside, text="Class:", font=("times new roman", 13, "bold"), bg="white")
        ClassLabel.grid(row=1, column=2, padx=10, pady=8, sticky=W)
        ClassEntry = ttk.Entry(left_inside, textvariable=self.attenClass, width=20, font=("times new roman", 13, "bold"))
        ClassEntry.grid(row=1, column=3, padx=10, pady=8, sticky=W)

        # Date attendance
        DateLabel = Label(left_inside, text="Date:", font=("times new roman", 13, "bold"), bg="white")
        DateLabel.grid(row=2, column=0, padx=10, pady=8, sticky=W)
        DateEntry = ttk.Entry(left_inside, textvariable=self.attenDate, width=20, font=("times new roman", 13, "bold"))
        DateEntry.grid(row=2, column=1, padx=10, pady=8, sticky=W)

        # Time attendance
        TimeLabel = Label(left_inside, text="Time:", font=("times new roman", 13, "bold"), bg="white")
        TimeLabel.grid(row=2, column=2, padx=10, pady=8, sticky=W)
        TimeEntry = ttk.Entry(left_inside, textvariable=self.attenTime, width=20, font=("times new roman", 13, "bold"))
        TimeEntry.grid(row=2, column=3, padx=10, pady=8, sticky=W)

        # Status attendance
        StatusLabel = Label(left_inside, text="Status:", font=("times new roman", 13, "bold"), bg="white")
        StatusLabel.grid(row=3, column=0, padx=10, pady=8, sticky=W)
        self.atten_status = ttk.Combobox(left_inside, textvariable=self.attenStatus, width=18, font=("times new roman", 13, "bold"), state="readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1, padx=10, pady=8, sticky=W)
        self.atten_status.current(0)

        # button frame
        btnFrame = Frame(left_inside, bd=2, relief=RIDGE, bg="white")
        btnFrame.place(x=0, y=300, width=715, height=35)

        btnImport = Button(btnFrame, text="Import", width=17, command=self.importCSV, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnImport.grid(row=0, column=0)

        btnExport = Button(btnFrame, text="Export", width=17, command=self.exportCSV, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnExport.grid(row=0, column=1)

        btnUpdate = Button(btnFrame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnUpdate.grid(row=0, column=2)

        btnReset = Button(btnFrame, text="Reset", width=17, command=self.reset_data, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnReset.grid(row=0, column=3)



        # Right label frame
        RightFrame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details",
                                font=("times new roman", 13, "bold"))
        RightFrame.place(x=750, y=10, width=730, height=580)

        tableFrame = Frame(RightFrame, bd=2, relief=RIDGE, bg="white")
        tableFrame.place(x=5, y=5, width=720, height=480)

        # scroll bar table_______________________________________________________________________________
        scroll_x = ttk.Scrollbar(tableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableFrame, orient=VERTICAL)

        self.ReportTable = ttk.Treeview(tableFrame, column=("id", "name", "mssv", "class", "date", "time", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.ReportTable.xview)
        scroll_y.config(command=self.ReportTable.yview)

        self.ReportTable.heading("id", text="STT")
        self.ReportTable.heading("name", text="Name")
        self.ReportTable.heading("mssv", text="MSSV")
        self.ReportTable.heading("class", text="Class")
        self.ReportTable.heading("date", text="Date")
        self.ReportTable.heading("time", text="Time")
        self.ReportTable.heading("attendance", text="Attendance")

        self.ReportTable["show"] = "headings"
        self.ReportTable.column("id", width=30)
        self.ReportTable.column("name", width=150)
        self.ReportTable.column("mssv", width=80)
        self.ReportTable.column("class", width=50)
        self.ReportTable.column("date", width=50)
        self.ReportTable.column("time", width=50)
        self.ReportTable.column("attendance", width=50)

        self.ReportTable.pack(fill=BOTH, expand=1)

        self.ReportTable.bind("<ButtonRelease>", self.get_cursor)

    # fetch data________________________________________________________
    def showData(self, rows):
        self.ReportTable.delete(*self.ReportTable.get_children())
        for i in rows:
            self.ReportTable.insert("", END, values=i)


    # import csv _________________________________________________________
    def importCSV(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(), title="Open csv", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)
            self.showData(mydata)
    # export csv _________________________________________________________
    def exportCSV(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No data", "Data not found to export", parent=self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Open csv",
                                             filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
            with open(fln, mode="w", newline="") as myfile:
                expWrite = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    expWrite.writerow(i)
                messagebox.showinfo("Data export", "Your data exported to "+os.path.basename(fln)+" successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    def get_cursor(self, event=""):
        cursor_row = self.ReportTable.focus()
        content = self.ReportTable.item(cursor_row)
        rows = content['values']
        self.attenID.set(rows[0])
        self.attenName.set(rows[1])
        self.attenMSSV.set(rows[2])
        self.attenClass.set(rows[3])
        self.attenDate.set(rows[4])
        self.attenTime.set(rows[5])
        self.attenStatus.set(rows[6])

    def reset_data(self):
        self.attenID.set("")
        self.attenName.set("")
        self.attenMSSV.set("")
        self.attenClass.set("")
        self.attenDate.set("")
        self.attenTime.set("")
        self.attenStatus.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()