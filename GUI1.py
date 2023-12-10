import tkinter as tk
root =tk.Tk()
root.title("My Gui app")
root.geometry("600x700")
mylabel = tk.Label(root, text = "This is my first python GUI",

                  fg = "blue", bg = "white", font = 14).pack(padx=10, pady=20)
button = tk.Button(root, text="Please click me", bg= "red").pack()
canvas = tk.Canvas(root, bg = "blue" ).pack()
entry = tk.Entry(root, bg = "white").pack()
frame = tk.Frame(root).pack(padx = 20, pady = 20)
entry = tk.Entry(frame, bg = "white").pack(side = "left",padx = 20)
button = tk.Button(frame, text="Save here").pack(side = "right", padx=20)
#BUTTON WITH COMMAND
def hi():

    label = tk.Label(root, text= "Welcome to python class").pack()

btn1 = tk.Button(root, text = "Greetingsss!", bg = "white" ,command = hi).pack()

entry1 = tk.Entry(root, bg = "white").pack()
entry2 = tk.Entry(root, bg = "white").pack()
btn1 = tk.Button(root, text = "Calculate!", bg = "white" ,command = None).pack()

root.mainloop()
