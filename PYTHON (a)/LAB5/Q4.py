from tkinter import *
import pymysql as my

conn = my.connect(
    host="172.21.170.10",
    user="msc",
    password="msc",
    database="msc"
)
cursor = conn.cursor()

root = Tk()
font = ("Arial", 20)

sname = StringVar()
registrationid = IntVar()
coursename = StringVar()
semester = IntVar()

label1 = Label(root, text="Name : ")
label1.grid(row=0, column=0)
name = Entry(root, font=font, textvariable=sname)
name.grid(row=0, column=1, padx=5, pady=5)

label2 = Label(root, text="Reg. ID : ")
label2.grid(row=1, column=0)
reg_id = Entry(root, font=font, textvariable=registrationid)
reg_id.grid(row=1, column=1, padx=5, pady=5)

label3 = Label(root, text="Course : ")
label3.grid(row=2, column=0)
course = Entry(root, font=font, textvariable=coursename)
course.grid(row=2, column=1, padx=5, pady=5)

label3 = Label(root, text="Sem : ")
label3.grid(row=3, column=0)
sem = Entry(root, font=font, textvariable=semester)
sem.grid(row=3, column=1, padx=5, pady=5)

def submit():
    n  = sname.get()
    i = registrationid.get()
    c = coursename.get()
    s = semester.get()
    cursor.execute("INSERT INTO student40(name, reg_id, course, sem) VALUES (%s, %s, %s, %s)", (n, i, c, s))
    conn.commit()
    print("value added successfully")


btn = Button(root, text="Submit", command=submit, font=("Arial", 10), compound = 'bottom')
btn.grid(row=4, column=1)


root.mainloop()