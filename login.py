from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
from main import FaceRecognitionSystem

def main():
    win = Tk()
    app = Login(win)
    win.mainloop()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x800+0+0")
        self.root.title("Face recognition system")

        self.bg = ImageTk.PhotoImage(file="image/BgBlue.png")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open("image/user_icon.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)
        get_start = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_start.place(x=95, y=100)

        #label
        lblUsername = Label(frame, text="User name", font=("times new roman", 15, "bold"), fg="white", bg="black")
        lblUsername.place(x=70, y=155)

        self.txtUser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtUser.place(x=40, y=185, width=270)

        lblPassword = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        lblPassword.place(x=70, y=225)

        self.txtPassword = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtPassword.place(x=40, y=255, width=270)

        # icon image_____________________________________
        img2 = Image.open("image/user_icon.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("image/lock_icon.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        # login button______________________________
        btnLogin = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), cursor="hand2", bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        btnLogin.place(x=110, y=300, width=120, height=35)

        # register button_________________________________
        btnSignUp = Button(frame, command=self.register_window, text="Sign up an account", font=("times new roman", 12, "bold"), cursor="hand2", borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        btnSignUp.place(x=20, y=350, width=160)

        # forgot pass button________________________________
        btnForgot = Button(frame, command=self.forgot_password, text="Forgot your password", font=("times new roman", 12, "bold"), cursor="hand2", borderwidth=0, fg="white",
                          bg="black", activeforeground="white", activebackground="black")
        btnForgot.place(x=30, y=375, width=160)

    # Hiển thị của sổ đăng ký
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

    def login(self):
        if self.txtUser.get()=="" or self.txtPassword.get()=="":
            messagebox.showerror("Error", "All field required")
        elif self.txtUser.get()=="admin" and self.txtPassword.get()=="123":
            messagebox.showinfo("Success", "Login successful")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%s and pass=%s", (
                self.txtUser.get(),
                self.txtPassword.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                open_main = messagebox.askyesno("Yes or n", "Access only admin")
                if open_main>0:
                        self.new_window = Toplevel(self.root)
                        self.app = FaceRecognitionSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    # Reset password________________________________________________________________
    def reset_pass(self):
        if self.txt_email.get()=="":
            messagebox.showerror("Error", "Enter email", parent=self.root2) #Nếu không có parent=self.root2 thì bấm nút reset sẽ nhả về trang đăng nhập
        elif self.txt_phone.get()=="":
            messagebox.showerror("Error", "Enter phone", parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error", "Enter new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
            my_cursor = conn.cursor()
            query1 = ("select * from register where email=%s")
            value1 = (self.txtUser.get(), self.txt_email.get(), self.txt_phone.get(),)
            my_cursor.execute(query1, value1)
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error", "Please enter correct your email and phone", parent=self.root2)
            else:
                query2=("update register set pass=%s where email=%s")
                value2=(self.txt_newpass.get(), self.txtUser.get())
                my_cursor.execute(query2, value2)

                conn.commit()
                conn.close()
                messagebox.showinfo("Information", "Your password has been reset", parent=self.root2)

    # forgot password_______________________________________________________________
    def forgot_password(self):
        if self.txtUser.get()=="":
            messagebox.showerror("Error", "Please write the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="haihai20", database="project3")
            my_cursor = conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtUser.get(),)
            my_cursor.execute(query, value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("My Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                email = Label(self.root2, text="Email:", font=("times new roman", 16, "bold"), fg="black", bg="white")
                email.place(x=50, y=80)

                self.txt_email = ttk.Entry(self.root2, font=("times new roman", 16, "bold"))
                self.txt_email.place(x=50, y=110, width=250)

                phone = Label(self.root2, text="Phone:", font=("times new roman", 16, "bold"), fg="black", bg="white")
                phone.place(x=50, y=150)

                self.txt_phone = ttk.Entry(self.root2, font=("times new roman", 16, "bold"))
                self.txt_phone.place(x=50, y=180, width=250)

                newpass = Label(self.root2, text="New password:", font=("times new roman", 16, "bold"), fg="black", bg="white")
                newpass.place(x=50, y=220)

                self.txt_newpass = ttk.Entry(self.root2, font=("times new roman", 16, "bold"))
                self.txt_newpass.place(x=50, y=250, width=250)

                btn=Button(self.root2, text="Reset", command=self.reset_pass, font=("times new roman", 16, "bold"), fg="white", bg="green")
                btn.place(x=100, y=290)


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
    obj = Login(root)
    root.mainloop()