from tkinter import *
import threading

pick = 0
label_list = []
i = 2
label3 = Label
m = 0

def yusefusi():
    global pick
    pick = m-1
    label_list[pick]["bg"] = "red"
    timer = threading.Timer(0.7, update)
    timer.start()

def update():
    global pick
    global i
    time = m
    while time != 0:
        pick = (pick+1) % 64
        if label_list[pick]["bg"] == "green":
            time -= 1
    label_list[pick]["bg"] = "red"
    global label3
    label3["text"] = "f(%d)" % i
    i += 1
    if i <= 63:
        timer = threading.Timer(0.7, update)
        timer.start()

def ans():
    root1 = Tk()
    root1.title('约瑟夫斯问题')
    root1.geometry("1200x675+360+200")
    tag_list = []
    for i in range(64):
        label_list.append(Label(root1, text="%d" % i, bg="green", font=20))
        label_list[i].place(x=(i % 8)*70+300, y=(i//8)*70+100)
        tag_list.append(i)
    global label3
    label3 = Label(root1, text="f(1)", font=20)
    label3.place(x=580, y=50)
    global m
    m = eval(e1.get())
    yusefusi()
    root.destroy()
    root1.mainloop()

root = Tk()
root.title('约瑟夫斯问题')
root.geometry("1200x675+360+200")
Label1 = Label(root, text="请输入指定的数:", font=20)
Label1.place(x=400, y=300)
e1 = Entry(root)
e1.place(x=590, y=305, width=30)
Label2 = Label(root, text="默认学生人数n为64", font=20)
Label2.place(x=410, y=220)
b1 = Button(root, text='确定', font='20', command=ans)
b1.place(x=630, y=290, width=60)
root.mainloop()
