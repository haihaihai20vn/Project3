from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        title_lbl = Label(self.root, text="DEVELOPER", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("image/dev.png")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoImage_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoImage_top)
        f_lbl.place(x=0, y=45, width=1530, height=720)

        main_frame = Frame(f_lbl, bd=2, bg="white")
        main_frame.place(x=1000, y=0, width=500, height=600)

        img_top1 = Image.open("image/dev.png")
        img_top1 = img_top.resize((200, 200), Image.ANTIALIAS)
        self.photoImage_top1 = ImageTk.PhotoImage(img_top1)

        f_lbl = Label(main_frame, image=self.photoImage_top1)
        f_lbl.place(x=300, y=0, width=200, height=200)

        # Developer info
        DevLabel = Label(main_frame, text="Hello", font=("times new roman", 13, "bold"), bg="white")
        DevLabel.place(x=0, y=5)

        DevLabel = Label(main_frame, text="I am studying ĐHBKHN", font=("times new roman", 13, "bold"), bg="white")
        DevLabel.place(x=0, y=40)

        img2 = Image.open("image/StudentRight.jpg")
        img2 = img2.resize((500, 390), Image.ANTIALIAS)
        self.photoImage2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(main_frame, image=self.photoImage2)
        f_lbl.place(x=0, y=210, width=500, height=390)

if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()