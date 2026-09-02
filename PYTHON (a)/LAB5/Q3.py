import tkinter as tk
from tkinter import ttk, messagebox

def display_answers():
    rating = rating_var.get()

    selected_topics = []
    if topic1.get():
        selected_topics.append("GUI Programming")
    if topic2.get():
        selected_topics.append("Data Science")
    if topic3.get():
        selected_topics.append("Web Development")
    
    topics_str = ", ".join(selected_topics) if selected_topics else "None selected"

    semester = combo_semester.get()
    
    result_text = (
        f"--- Survey Results ---\n\n"
        f"Python Rating: {rating}\n"
        f"Liked Topics: {topics_str}\n"
        f"Semester: {semester}"
    )
    
    messagebox.showinfo("Survey Submission", result_text)
\
root = tk.Tk()
root.title("Student Survey Form")

l1 = tk.Label(root, text="Question 1: How do you rate Python?")
l1.pack(anchor="w", pady=(5, 5))

rating_var = tk.StringVar()
ratings = ["Excellent", "Good", "Average", "Poor"]

for rate in ratings:
    rb = tk.Radiobutton(root, text=rate, value=rate, variable=rating_var)
    rb.pack(anchor = "w", padx=10)

l2 = tk.Label(root, text="\nQuestion 2: Which topics do you like?")
l2.pack(anchor = "w", pady = 5)

topic1 = tk.BooleanVar()
topic2 = tk.BooleanVar()
topic3 = tk.BooleanVar()

cbtn1 = tk.Checkbutton(root, text="GUI Programming", variable=topic1)
cbtn1.pack(anchor = "w", padx=10)

cbtn2 = tk.Checkbutton(root, text="Data Science", variable=topic2)
cbtn2.pack(anchor = "w", padx=10)

cbtn3 = tk.Checkbutton(root, text="Web Development", variable=topic3)
cbtn3.pack(anchor = "w", padx=10)

l3 = tk.Label(root, text="\nQuestion 3: Which semester are you in?", font=("Arial", 10, "bold"))
l3.pack(anchor = "w", pady=5)

combo_semester = ttk.Combobox(root, 
    values=["Semester 1", "Semester 2", "Semester 3", "Semester 4", "Semester 5", "Semester 6"],
    state="readonly", width=30
)
combo_semester.pack(anchor="w", padx=10, pady=(0, 15))


btn_submit = tk.Button(root, text="Submit & View Answers", command=display_answers)
btn_submit.pack(pady = 5)

root.mainloop()