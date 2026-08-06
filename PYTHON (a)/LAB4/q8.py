import tkinter as tk
window = tk.Tk()

window.geometry("500x600")
window.title("Pizza Slice Shop")

label1 = tk.Label(window, text="Order Your Pizza" , font= ("arial", 20 , "bold"))
label1.pack()

label2 = tk.Label(window, text="Choose Size", font=("arial" , 12))
label2.pack()

sizes = ["Small (Rs 8.00)", "Medium (Rs 11.00)" , "Large (Rs 14.00)"]
x = Intvar()
for size in sizes:
  radiob = tk.Radiobutton


window.mainloop()