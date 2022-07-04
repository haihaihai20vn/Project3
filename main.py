import tkinter.messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        #first image
        '''img = Image.open("D:/python/Webcam/img/Mark.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoImage = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoImage)
        f_lbl.place(x=0, y=0, width=500, height=130)'''

        # second image
        img1 = Image.open("image/Header.jpg")
        img1 = img1.resize((1530, 130), Image.ANTIALIAS)
        self.photoImage1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoImage1)
        f_lbl.place(x=0, y=0, width=1530, height=130)

        # three image
        '''img2 = Image.open("D:/python/Webcam/img/Mark.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoImage2)
        f_lbl.place(x=1000, y=0, width=550, height=130)'''

        #bg image
        img3 = Image.open("image/BgBlue.png")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoImage3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoImage3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # time_______________________________________
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text=string)
            lbl.after(1000, time)
        lbl = Label(title_lbl, font=("times new roman", 14, "bold"), background='white', foreground='blue')
        lbl.place(x=0, y=0, width=110, height=50)
        time()

        #student button
        img4 = Image.open("image/StudentIcon.PNG")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoImage4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoImage4, command=self.StudentDetails, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Student Details", command=self.StudentDetails, cursor="hand2", font=("times new roman", 16, "bold"), bg="red", fg="white")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Detect face button
        img5 = Image.open("image/FaceDetectIcon.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoImage5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoImage5, cursor="hand2", command=self.FaceRecognition)
        b1.place(x=500, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Face Detection", cursor="hand2", command=self.FaceRecognition, font=("times new roman", 16, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=500, y=300, width=220, height=40)

        # Attendance face button
        img6 = Image.open("image/AttendanceIcon.png")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoImage6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoImage6, cursor="hand2", command=self.AttendanceScreen)
        b1.place(x=800, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", command=self.AttendanceScreen, font=("times new roman", 16, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=800, y=300, width=220, height=40)

        # Help button
        img7 = Image.open("image/HelpIcon.png")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoImage7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoImage7, cursor="hand2", command=self.HelpScreen)
        b1.place(x=1100, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Help", cursor="hand2", command=self.HelpScreen, font=("times new roman", 16, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=1100, y=300, width=220, height=40)

        # Train data button
        img8 = Image.open("image/TrainDataIcon.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoImage8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoImage8, cursor="hand2", command=self.TrainData)
        b1.place(x=200, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Train data", cursor="hand2", command=self.TrainData, font=("times new roman", 16, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=200, y=580, width=220, height=40)

        # Photos button
        img9 = Image.open("image/PhotoIcon.png")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoImage9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoImage9, cursor="hand2", command=self.open_img)
        b1.place(x=500, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 16, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=500, y=580, width=220, height=40)

        #Developer button
        img10 = Image.open("image/DeveloperIcon.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoImage10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoImage10, cursor="hand2", command=self.DeveloperScreen)
        b1.place(x=800, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Developer", cursor="hand2", command=self.DeveloperScreen, font=("times new roman", 16, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=800, y=580, width=220, height=40)

        # Introduce button
        img11 = Image.open("image/IntroduceIcon.png")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoImage11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoImage11, cursor="hand2", command=self.isExit)
        b1.place(x=1100, y=380, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", command=self.isExit, font=("times new roman", 16, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=1100, y=580, width=220, height=40)

    def open_img(self):
        os.startfile("data")

    def isExit(self):
        self.isExit = tkinter.messagebox.askyesno("Face regconition", "Are you sure exit?")
        if self.isExit > 0:
            self.root.destroy()
        else:
            return

    # ----------------Function buttons--------------------
    def StudentDetails(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def TrainData(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def FaceRecognition(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def AttendanceScreen(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def DeveloperScreen(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def HelpScreen(self):
        self.new_window = Toplevel(self.root)
        self.app = Help(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
