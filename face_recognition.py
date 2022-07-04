from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from time import strftime
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face recognition system")

        title_lbl = Label(self.root, text="FACE RECOGNITION", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # Left image
        img_left = Image.open("image/FaceRecognitionLeft.jpg")
        img_left = img_left.resize((650, 700), Image.ANTIALIAS)
        self.photoImage_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(self.root, image=self.photoImage_left)
        f_lbl.place(x=0, y=55, width=650, height=700)

        # Right image
        img_right = Image.open("image/FaceRecognitionRight.jpg")
        img_right = img_right.resize((950, 700), Image.ANTIALIAS)
        self.photoImage_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(self.root, image=self.photoImage_right)
        f_lbl.place(x=650, y=55, width=950, height=700)

        b1_1 = Button(f_lbl, text="FACE RECOGNITION", cursor="hand2", command=self.face_recognite, font=("times new roman", 18, "bold"), bg="red",
                      fg="white")
        b1_1.place(x=365, y=620, width=270, height=40)

    # attendance________________________________________________
    def attendance(self, i, n, c, k):
        with open("attendance.csv", "r+", newline="\n") as f:
            dataList = f.readlines()
            nameList = []
            for line in dataList:
                entry = line.split((",")) #hai, 2, K63
                nameList.append(entry[0])
            if((i not in nameList) and (n not in nameList) and (c not in nameList) and (k not in nameList)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {n}, {c}, {k},{d1}, {dtString}, Present")

    # Face recognition__________________________________________
    def face_recognite(self):
        def draw_boundary(img, classifier, scaleFacor, minNeigbor, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFacor, minNeigbor)
            coord = []
            for(x,y,w,h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(host="localhost", username="root", password="haihai20",
                                               database="project3")
                my_cursor = conn.cursor()
                my_cursor.execute("select Name from student where ID="+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                my_cursor.execute("select Class from student where ID=" + str(id))
                c = my_cursor.fetchone()
                c = "+".join(c)

                my_cursor.execute("select Course from student where ID=" + str(id))
                k = my_cursor.fetchone()
                k = "+".join(k)

                my_cursor.execute("select ID from student where ID=" + str(id))
                i = my_cursor.fetchone()
                i = "+".join(i)

                if confidence > 77:
                    cv2.putText(img, f"ID:{i}", (x, y - 75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"MSSV:{c}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(img, f"Course:{k}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    self.attendance(i, n, c, k)
                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, y]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1, 10, (255, 25, 255), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml") # file train: clf.write("classifier.xml")

        video = cv2.VideoCapture(0)

        while True:
            ret, img = video.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognition system", img)
            if cv2.waitKey(1) == 81:
                break
                video.release()
                cv2.destroyAllWindows()



if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()