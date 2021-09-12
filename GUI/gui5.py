# Geometry Managers : -->  grid() 

import tkinter as tk

win=tk.Tk()
win.geometry("500x400")
for i in range(10):
    for j in range(10):
        frame=tk.Frame(master=win,relief=tk.RAISED,borderwidth=1)
        frame.grid(row=i,column=j,padx=10,pady=10)
        label=tk.Label(master=frame,text=f"Row {i} \n Column {j}")
        label.pack()
win.mainloop() 