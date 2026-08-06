# making class that's easier to build fast gui for small tasks


class A:
    import tkinter as tk

    print(dir())
    print(locals())

    def __init__(self):
        self.window = A.tk.Tk()

    def place_btn(self, text="default_text", func=print):
        A.tk.Button(text=text, command=func).pack()

    def runloop(self):
        self.window.mainloop()


def myfunc():
    print("hello")


a = A()
a.place_btn()
a.runloop()

# output:
# little window with one button button in the center
