from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        title_lbl = Label(self.root, text="HELP", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        img_top = Image.open("image/BgBlue.png")
        img_top = img_top.resize((1530, 720), Image.ANTIALIAS)
        self.photoImage_top = ImageTk.PhotoImage(img_top)

        f_lbl = Label(self.root, image=self.photoImage_top)
        f_lbl.place(x=0, y=45, width=1530, height=720)

        DevLabel = Label(f_lbl, text="Email: hai@gmail.com", font=("times new roman", 20, "bold"), fg="blue", bg="white")
        DevLabel.place(x=600, y=260)

if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()