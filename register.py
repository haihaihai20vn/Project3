from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # variables____________________________________________
        self.var_fname =StringVar()
        self.var_lname = StringVar()
        self.var_pass = StringVar()
        self.var_cofirm = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()

        self.bg = ImageTk.PhotoImage(file="image/BgBlue.png")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)


        # Left image____________________________________
        self.bg1 = ImageTk.PhotoImage(file="image/LeftRegister.PNG")
        bg_lbl1 = Label(self.root, image=self.bg1)
        bg_lbl1.place(x=50, y=100, width=470, height=550)

        # main frame______________________________________
        frame = Frame(self.root, bg="black")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="FORM REGISTER", font=("times new roman", 20, "bold"), fg="red", bg="black")
        register_lbl.place(x=20, y=20)

        # label and entry________________________________
        fname = Label(frame, text="First Name:", font=("times new roman", 16, "bold"), fg="white", bg="black")
        fname.place(x=50, y=100)

        self.fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 16, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        lname = Label(frame, text="Last Name:", font=("times new roman", 16, "bold"), fg="white", bg="black")
        lname.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 16, "bold"))
        self.txt_lname.place(x=370, y=130, width=250)

        password = Label(frame, text="Password:", font=("times new roman", 16, "bold"), fg="white", bg="black")
        password.place(x=50, y=170)

        self.txt_pass = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 16, "bold"))
        self.txt_pass.place(x=50, y=200, width=250)

        confirm = Label(frame, text="Confirm password:", font=("times new roman", 16, "bold"), fg="white", bg="black")
        confirm.place(x=370, y=170)

        self.txt_confirm = ttk.Entry(frame, textvariable=self.var_cofirm, font=("times new roman", 16, "bold"))
        self.txt_confirm.place(x=370, y=200, width=250)

        email = Label(frame, text="Email:", font=("times new roman", 16, "bold"), fg="white", bg="black")
        email.place(x=50, y=250)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 16, "bold"))
        self.txt_email.place(x=50, y=280, width=250)

        phone = Label(frame, text="Phone:", font=("times new roman", 16, "bold"), fg="white", bg="black")
        phone.place(x=370, y=250)

        self.txt_phone = ttk.Entry(frame, textvariable=self.var_phone, font=("times new roman", 16, "bold"))
        self.txt_phone.place(x=370, y=280, width=250)

        # check button ___________________________________________________
        self.var_check=IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree the tearms and conditions", font=("times new roman", 14, "bold"), fg="white", bg="black", onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=330)

        # button _________________________________________________________________
        img = Image.open("image/register.png")
        img = img.resize((200, 80), Image.ANTIALIAS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", bg="black")
        b1.place(x=30, y=400, width=200)

        img1 = Image.open("image/loginbtn.jpg")
        img1 = img1.resize((200, 70), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b1 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", bg="black")
        b1.place(x=350, y=400, width=200)

    # function______________________________________________________________________________
    def register_data(self):
        if self.var_fname.get()=="" or self.var_pass.get()=="" or self.var_email.get()=="":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get()!=self.var_cofirm.get():
            messagebox.showerror("Error", "Password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
            my_cursor = conn.cursor()
            query = ("select * from register where email=%s")
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "Email already exist, please try another email")
            else:
                my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_pass.get(),
                    self.var_cofirm.get(),
                    self.var_email.get(),
                    self.var_phone.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Register Successfully")




if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()