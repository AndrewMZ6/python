# raw procedural tkinter experimenting

import os
import tkinter as tk
import sys
from tkinter import ttk

# check the files in the working directory
files_list = os.listdir()
if "tkinter.py" in files_list:
    print('theres a file with name "tkinter in your directory"')
    os.remove("tkinter.py")

# created instance of class <class 'tkinter.Tk'>
win = tk.Tk()

frame = ttk.Frame()


# sys.exit()

# created instance of class <class 'tkinter.Label'>
# then called method "pack" of the instance
lab = ttk.Label(master=frame, text="Python rocks!")
lab.pack(side=tk.LEFT)


but = ttk.Button(master=frame, text="\N{RIGHTWARDS BLACK ARROW}")
but.pack(side=tk.LEFT)

en = ttk.Entry(master=frame)
en.pack(side=tk.LEFT)


t = tk.Text(master=frame)
t.pack(side=tk.LEFT)
frame.pack()
# start eventloop by running
# <bound method Misc.mainloop of <tkinter.Tk object .>>
win.mainloop()

# Widgets:
# 	Each widget in Tkinter is defined by a class.
# 	Some of them are:
# 		Label, Button, Entry, Text, Frame
#
# 	(master = Frame, ) -> keyword argument for assigning a widget to a Frame
#
# 	Geometry managers:
# 		.pack()			-> pack(side = tk.TOP)	, uses side as where to place
# 		.place()		-> place(x=50, y=75)	, uses coordinats valued in pixels. Origin (x=0, y=0) is top left
# 		.grid()			-> grid(row=0, column=1), uses matrix-like indexing
#
# 	Widget naming convention:
# 		Label  	->	lbl
# 		Button	->	btn
# 		Entry	->	ent
# 		Text	->	txt
# 		Frame	->	frm
#
# 	File opening window:
# 		from tkinter.filedialog import askopenfilename
