from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        # variables_______________________________________
        self.var_malop = StringVar()
        self.var_subject = StringVar()
        self.var_week = StringVar()
        self.var_semester = StringVar()
        self.var_id = StringVar()
        self.var_name = StringVar()
        self.var_class = StringVar()
        self.var_course = StringVar()
        self.var_birthday = StringVar()
        self.var_gender = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()



        # first image
        img = Image.open("image/StudentLeft.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=0, width=500, height=130)

        # second image
        img1 = Image.open("image/StudentCenter.jpg")
        img1 = img1.resize((550, 130), Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoImage1)
        f_lbl.place(x=500, y=0, width=500, height=130)

        # three image
        img2 = Image.open("image/StudentRight.jpg")
        img2 = img2.resize((550, 130), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoImage2)
        f_lbl.place(x=1000, y=0, width=550, height=130)

        # bg image
        img3 = Image.open("image/BgBlue.png")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoImage3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="STUDENT MANAGEMENT", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=10, y=55, width=1500, height=600)

        #Left label frame
        LeftFrame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        LeftFrame.place(x=10, y=10, width=730, height=580)

        img_left = Image.open("image/StudentDetails.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoImage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(LeftFrame, image=self.photoImage_left)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # Course information
        CourseFrame = LabelFrame(LeftFrame, bd=2, bg="white", relief=RIDGE, text="Course Infomation",
                               font=("times new roman", 12, "bold"))
        CourseFrame.place(x=5, y=135, width=720, height=115)

        #School
        '''SchoolLabel = Label(CourseFrame, text="School", font=("times new roman", 13, "bold"), bg="white")
        SchoolLabel.grid(row=0, column=0, padx=10)
        SchoolCombobox = ttk.Combobox(CourseFrame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        SchoolCombobox["values"] = ("Select School", "ME", "EEE", "IT", "SAMI")
        SchoolCombobox.current(0)
        SchoolCombobox.grid(row=0, column=1, padx=2, pady=10, sticky=W)'''
        # Ma lop
        MaLopLabel = Label(CourseFrame, text="Code class:", font=("times new roman", 13, "bold"), bg="white")
        MaLopLabel.grid(row=0, column=0, padx=10)
        MaLopEntry = ttk.Entry(CourseFrame, textvariable=self.var_malop, width=22, font=("times new roman", 13, "bold"))
        MaLopEntry.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # Subject
        SubjectLabel = Label(CourseFrame, text="Subject", font=("times new roman", 13, "bold"), bg="white")
        SubjectLabel.grid(row=0, column=2, padx=10)
        SubjectCombobox = ttk.Combobox(CourseFrame,  textvariable=self.var_subject, font=("times new roman", 13, "bold"), state="readonly", width=20)
        SubjectCombobox["values"] = ("Select subject", "AI", "Project 1", "Project 3", "Math", "Physical")
        SubjectCombobox.current(0)
        SubjectCombobox.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # Week
        WeekLabel = Label(CourseFrame, text="Week", font=("times new roman", 13, "bold"), bg="white")
        WeekLabel.grid(row=1, column=0, padx=10)
        WeekCombobox = ttk.Combobox(CourseFrame, textvariable=self.var_week, font=("times new roman", 13, "bold"), state="readonly", width=20)
        WeekCombobox["values"] = ("Select week", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18")
        WeekCombobox.current(0)
        WeekCombobox.grid(row=1, column=1, padx=2, pady=10, sticky=W)

        # semester
        SemesterLabel = Label(CourseFrame, text="Semester", font=("times new roman", 13, "bold"), bg="white")
        SemesterLabel.grid(row=1, column=2, padx=10, sticky=W)
        SemesterCombobox = ttk.Combobox(CourseFrame, textvariable=self.var_semester, font=("times new roman", 13, "bold"), state="readonly", width=20)
        SemesterCombobox["values"] = ("Select semester", "20211", "20212", "20213", "20221")
        SemesterCombobox.current(0)
        SemesterCombobox.grid(row=1, column=3, padx=2, pady=10, sticky=W)

        # Class student information
        ClassFrame = LabelFrame(LeftFrame, bd=2, bg="white", relief=RIDGE, text="Student Infomation",
                                 font=("times new roman", 12, "bold"))
        ClassFrame.place(x=5, y=260, width=720, height=290)

        #Student id
        StudentIDLabel = Label(ClassFrame, text="ID:", font=("times new roman", 13, "bold"), bg="white")
        StudentIDLabel.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        StudentIDEntry = ttk.Entry(ClassFrame, textvariable=self.var_id, width=20, font=("times new roman", 13, "bold"))
        StudentIDEntry.grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Student name
        StudentNameLabel = Label(ClassFrame, text="Full name:", font=("times new roman", 13, "bold"), bg="white")
        StudentNameLabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)
        StudentNameEntry = ttk.Entry(ClassFrame, textvariable=self.var_name, width=20, font=("times new roman", 13, "bold"))
        StudentNameEntry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        # Class
        StudentClassLabel = Label(ClassFrame, text="MSSV:", font=("times new roman", 13, "bold"), bg="white")
        StudentClassLabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        StudentClassEntry = ttk.Entry(ClassFrame, textvariable=self.var_class, width=20, font=("times new roman", 13, "bold"))
        StudentClassEntry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Course
        CourseLabel = Label(ClassFrame, text="Course:", font=("times new roman", 13, "bold"), bg="white")
        CourseLabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)
        CourseEntry = ttk.Entry(ClassFrame, textvariable=self.var_course, width=20, font=("times new roman", 13, "bold"))
        CourseEntry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        # Birthday
        BirthdayLabel = Label(ClassFrame, text="Birthday:", font=("times new roman", 13, "bold"), bg="white")
        BirthdayLabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)
        BirthdayEntry = ttk.Entry(ClassFrame, textvariable=self.var_birthday, width=20,
                                font=("times new roman", 13, "bold"))
        BirthdayEntry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Gender
        GenderLabel = Label(ClassFrame, text="Gender:", font=("times new roman", 13, "bold"), bg="white")
        GenderLabel.grid(row=2, column=2, padx=10, pady=5, sticky=W)
        GenderCombobox = ttk.Combobox(ClassFrame, textvariable=self.var_gender, font=("times new roman", 13, "bold"),
                                    state="readonly", width=18)
        GenderCombobox["values"] = ("Male", "Female")
        GenderCombobox.current(0)
        GenderCombobox.grid(row=2, column=3, padx=10, pady=5, sticky=W)

        # Email
        EmailLabel = Label(ClassFrame, text="Email:", font=("times new roman", 13, "bold"), bg="white")
        EmailLabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)
        EmailEntry = ttk.Entry(ClassFrame, textvariable=self.var_email, width=20, font=("times new roman", 13, "bold"))
        EmailEntry.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Phone
        PhoneLabel = Label(ClassFrame, text="Phone:", font=("times new roman", 13, "bold"), bg="white")
        PhoneLabel.grid(row=3, column=2, padx=10, pady=5, sticky=W)
        PhoneEntry = ttk.Entry(ClassFrame, textvariable=self.var_phone, width=20, font=("times new roman", 13, "bold"))
        PhoneEntry.grid(row=3, column=3, padx=10, pady=5, sticky=W)



        # radio button
        self.var_radio1 = StringVar()
        radioBtn1 = ttk.Radiobutton(ClassFrame, variable=self.var_radio1, text="Take your photo", value="Yes")
        radioBtn1.grid(row=6, column=0, padx=10, pady=5)

        radioBtn2 = ttk.Radiobutton(ClassFrame, variable=self.var_radio1, text="No your photo", value="No")
        radioBtn2.grid(row=6, column=1)

        # button frame
        btnFrame = Frame(ClassFrame, bd=2, relief=RIDGE, bg="white")
        btnFrame.place(x=0, y=200, width=715, height=35)

        btnSave = Button(btnFrame, text="Save", command=self.add_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnSave.grid(row=0, column=0)

        btnUpdate = Button(btnFrame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnUpdate.grid(row=0, column=1)

        btnDelete = Button(btnFrame, text="Delete", command=self.delete_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnDelete.grid(row=0, column=2)

        btnReset = Button(btnFrame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnReset.grid(row=0, column=3)

        btnFrame1 = Frame(ClassFrame, bd=2, relief=RIDGE, bg="white")
        btnFrame1.place(x=0, y=235, width=715, height=35)

        btnTakePhoto = Button(btnFrame1, command=self.generate_dataset, text="Take photo", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnTakePhoto.grid(row=0, column=0)

        btnUpdatePhoto = Button(btnFrame1, text="Update photo", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnUpdatePhoto.grid(row=0, column=1)

        # Right label frame
        RightFrame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details",
                               font=("times new roman", 13, "bold"))
        RightFrame.place(x=750, y=10, width=730, height=580)

        img_right = Image.open("image/StudentSoftware.jpg")
        img_right = img_right.resize((720, 130), Image.ANTIALIAS)
        self.photoImage_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(RightFrame, image=self.photoImage_right)
        f_lbl.place(x=5, y=0, width=720, height=130)

        # Search
        SearchFrame = LabelFrame(RightFrame, bd=2, bg="white", relief=RIDGE, text="Search",
                                font=("times new roman", 12, "bold"))
        SearchFrame.place(x=5, y=135, width=710, height=70)

        SearchLabel = Label(SearchFrame, text="Search by:", font=("times new roman", 13, "bold"), bg="gray")
        SearchLabel.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        SearchCombobox = ttk.Combobox(SearchFrame, font=("times new roman", 13, "bold"), state="readonly", width=15)
        SearchCombobox["values"] = ("Select", "ID", "Name")
        SearchCombobox.current(0)
        SearchCombobox.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        SearchEntry = ttk.Entry(SearchFrame, width=20, font=("times new roman", 13, "bold"))
        SearchEntry.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        btnSearch = Button(SearchFrame, text="Search", width=10, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnSearch.grid(row=0, column=3, padx=4)

        btnShowAll = Button(SearchFrame, text="Show All", width=10, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        btnShowAll.grid(row=0, column=4, padx=4)

        # table data
        TableFrame = Frame(RightFrame, bd=2, bg="white", relief=RIDGE)
        TableFrame.place(x=5, y=210, width=710, height=350)
        scroll_x = ttk.Scrollbar(TableFrame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(TableFrame, orient=VERTICAL)

        self.StudentTable = ttk.Treeview(TableFrame, column=("malop", "subject", "week", "semester", "id", "name", "class", "course", "birthday", "gender", "email", "phone", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.StudentTable.xview)
        scroll_y.config(command=self.StudentTable.yview)

        self.StudentTable.heading("malop", text="Code class")
        self.StudentTable.heading("subject", text="Subject")
        self.StudentTable.heading("week", text="Week")
        self.StudentTable.heading("semester", text="Semester")
        self.StudentTable.heading("id", text="ID")
        self.StudentTable.heading("name", text="Name")
        self.StudentTable.heading("class", text="MSSV")
        self.StudentTable.heading("course", text="Course")
        self.StudentTable.heading("birthday", text="Birthday")
        self.StudentTable.heading("gender", text="Gender")
        self.StudentTable.heading("email", text="Email")
        self.StudentTable.heading("phone", text="Phone")
        self.StudentTable.heading("photo", text="Photo")
        self.StudentTable["show"] = "headings"

        self.StudentTable.column("malop", width=100)
        self.StudentTable.column("subject", width=100)
        self.StudentTable.column("week", width=100)
        self.StudentTable.column("semester", width=100)
        self.StudentTable.column("id", width=100)
        self.StudentTable.column("name", width=100)
        self.StudentTable.column("class", width=100)
        self.StudentTable.column("course", width=100)
        self.StudentTable.column("birthday", width=100)
        self.StudentTable.column("gender", width=100)
        self.StudentTable.column("email", width=100)
        self.StudentTable.column("phone", width=100)
        self.StudentTable.column("photo", width=150)

        self.StudentTable.pack(fill=BOTH, expand=1)
        self.StudentTable.bind("<ButtonRelease>", self.get_cursor)
        self.show_data()

    # function________________________________________________
    def add_data(self):
        if self.var_subject.get() == "Select subject" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "Do not empty!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_malop.get(),
                    self.var_subject.get(),
                    self.var_week.get(),
                    self.var_semester.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_class.get(),
                    self.var_course.get(),
                    self.var_birthday.get(),
                    self.var_gender.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.show_data()
                conn.close()
                messagebox.showinfo("Notice", "Student information has been added successfully", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # show data_________________________________________
    def show_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()
        if len(data) != 0:
            self.StudentTable.delete(*self.StudentTable.get_children())
            for i in data:
                self.StudentTable.insert("", END, values=i)
            conn.commit()
        conn.close()

    # get cursor_________________________________________
    def get_cursor(self, event=""):
        cursor_focus = self.StudentTable.focus()
        content = self.StudentTable.item(cursor_focus)
        data = content["values"]

        self.var_malop.set(data[0]),
        self.var_subject.set(data[1]),
        self.var_week.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_id.set(data[4]),
        self.var_name.set(data[5]),
        self.var_class.set(data[6]),
        self.var_course.set(data[7]),
        self.var_birthday.set(data[8]),
        self.var_gender.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_radio1.set(data[12])

    # update function
    def update_data(self):
        if self.var_subject.get() == "Select subject" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "Do not empty!", parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update", "Do you want to update?", parent=self.root)
                if update>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Malop=%s, Subject=%s, Week=%s, Semester=%s, Name=%s, Class=%s, Course=%s, Birthday=%s, Gender=%s, Email=%s, Phone=%s, Photo=%s where ID=%s",(
                        self.var_malop.get(),
                        self.var_subject.get(),
                        self.var_week.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_class.get(),
                        self.var_course.get(),
                        self.var_birthday.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "Student information updated successfully!", parent=self.root)
                conn.commit()
                self.show_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # delete function_________________________________________
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error", "ID can not empty", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want delete this student?", parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
                    my_cursor = conn.cursor()
                    sql="delete from student where ID=%s"
                    val=(self.var_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.show_data()
                conn.close()
                messagebox.showinfo("Success", "Student information deleted successfully!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # reset function______________________________________
    def reset_data(self):
        self.var_malop.set("")
        self.var_subject.set("Select subject")
        self.var_week.set("Select week")
        self.var_semester.set("Select semester")
        self.var_id.set("")
        self.var_name.set("")
        self.var_class.set("")
        self.var_course.set("")
        self.var_birthday.set("")
        self.var_gender.set("Male")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_radio1.set("")

    # Generate data set or take photos
    def generate_dataset(self):
        if self.var_subject.get() == "Select subject" or self.var_name.get()=="" or self.var_id.get()=="":
            messagebox.showerror("Error", "Do not empty!", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                result=my_cursor.fetchall()
                id=0
                for x in result:
                    id+=1
                my_cursor.execute("update student set Malop=%s, Subject=%s, Week=%s, Semester=%s, Name=%s, Class=%s, Course=%s, Birthday=%s, Gender=%s, Email=%s, Phone=%s, Photo=%s where ID=%s",(
                        self.var_malop.get(),
                        self.var_subject.get(),
                        self.var_week.get(),
                        self.var_semester.get(),
                        self.var_name.get(),
                        self.var_class.get(),
                        self.var_course.get(),
                        self.var_birthday.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_radio1.get(),
                        self.var_id.get()==id+1
                    ))
                conn.commit()
                self.show_data()
                self.reset_data()
                conn.close()

                # load data on frontals face from opencv______
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_crooped(img):
                    gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray, 1.3, 5) #scaling factor=1.3, minimum neighbor=5
                    for(x,y,w,h) in faces:
                        face_crooped=img[y:y+h, x:x+w]
                        return face_crooped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret, frame=cap.read()
                    if face_crooped(frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_crooped(frame), (450,450))
                        face=cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user." + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Crooped Face", face)
                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating dataset completed!!!")
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()