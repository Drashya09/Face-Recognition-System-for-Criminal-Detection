from tkinter import *
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
from subprocess import call


def register():
    call(["python", "registerGUI.py"])
def VideoSurveillance():
    call(["python", "surveillance.py"])
def detectCriminal():
    call(["python", "detect.py"])


root = Tk()
root.geometry('1350x720')
root.minsize(1350,720)
#root.maxsize(800,500)
root.state("zoomed")


root.title("Face Recognition System for Criminal Detection")
root.configure(bg="#9AFEFF")


Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""
image=Image.open("image.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=1500,height=0,bg='#9AFEFF').place(x=0,y=0)
photo_label

label_0 = Label(root, text="Face Recognition System for Criminal Detection",width=82,height=3,font=("bold", 25),anchor=CENTER,bg="#123456",fg="white")
label_0.place(x=0,y=100)

Button(root, text='REGISTER CRIMINAL',width=35,height=3,bg='#87AFC7',fg='black',font=("bold", 12),command=register).place(x=420,y=330)
Button(root, text='PHOTO MATCH',width=35,height=3,bg='#87AFC7',fg='black',font=("bold", 12),command=detectCriminal).place(x=420,y=410)
Button(root, text='VIDEO SURVEILLANCE',width=35,height=3,bg='#15317E',fg='white',font=("bold", 12),command=VideoSurveillance).place(x=420,y=490)

image1 = Image.open("image1.jpg")
photo1 = ImageTk.PhotoImage(image1)
photo1_label = Label(image=photo1,width=380,height=380).place(x=900,y=270)
photo1_label

label_0 = Label(root,width=230,height=720,anchor=CENTER,bg="#123456")
label_0.place(x=0,y=700)

root.mainloop()