#6 create a GUI using tkinter module
import tkinter as tk

w = tk.Tk()
w.title("GUI example")
w.geometry("600x400")  # Corrected the typo here
label = tk.Label(w, text="Welcome to AIMCA, Bhatkal. by Using Tkinter!")
label.pack()
button = tk.Button(w, text="Click me!", command=w.destroy)
button.pack()
w.mainloop()
