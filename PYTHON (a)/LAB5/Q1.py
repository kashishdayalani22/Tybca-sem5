import tkinter as tk

def count_characters():
    content = text.get("1.0", "end-1c")
    char_count = len(content)
    l1.config(text=f"Character Count: {char_count}")

root = tk.Tk()

text = tk.Text(root, height=8, width=35)
text.pack(pady=5)

CB = tk.Button(root, text="Count Characters", command=count_characters)
CB.pack(pady=5)

l1 = tk.Label(root, text="Character Count: 0", font=("Arial", 10, "bold"))
l1.pack(pady=5)

root.mainloop()