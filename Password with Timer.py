import tkinter
import time
from time import sleep
from threading import Thread

def click_right():
    pass

def down_timer(secs):
    global lbl_time

#for i in range (0,secs):change from
for i in range(60, -1, -1):
    #The same applies below.
    sleep(1)
    lbl_time.config(text = str(i)) # type: ignore

root=tkinter.Tk()
root.title('')

canvas=tkinter.Canvas(root,width=800,height=600,bg='white')
canvas.pack()

btn_right=tkinter.Button(canvas,text='←attack',command=click_right)
btn_right.space(x=650,y=560)

character=['aaa','bbb']

lbl_time=tkinter.Label(canvas,width=25,font=('',40))
lbl_time.place(x=10,y=10)
lbl_time.config(text=str(10))

#Creating and Starting Threads
target_time=10
Thread_1=10
Thread(target=down_timer,args=(target_time,))
Thread_1.start()

#Mainloop
root.mainloop()
