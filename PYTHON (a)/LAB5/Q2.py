import tkinter as tk
from tkinter import messagebox

def submit_feedback():
    name = entry1.get()
    feedback = fb.get("1.0", tk.END).strip()

    messagebox.showinfo("Success", "Thank you! Your feedback has been submitted.")

root = tk.Tk()

l1 = tk.Label(root, text="Student Name:", font=("Arial", 10, "bold"))
l1.pack()
entry1 = tk.Entry(root, width=45)
entry1.pack(padx = 10)

l2 = tk.Label(root, text="Your Feedback:", font=("Arial", 10, "bold"))
l2.pack()
fb = tk.Text(root, height=8, width=45)
fb.pack(padx = 10)

btn = tk.Button(root, text="Submit Feedback", font=("Arial", 10, "bold"), command=submit_feedback)
btn.pack(pady = 10)

root.mainloop()