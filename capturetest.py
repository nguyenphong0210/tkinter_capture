from tkinter import *
from tkinter.ttk import *
import tkinter
import cv2
import PIL.Image, PIL.ImageTk
import time
import os
import defdetect as de

window = Tk()
window.title("Objects Detection Python")

cap = cv2.VideoCapture(0)

canvas_w = cap.get(cv2.CAP_PROP_FRAME_WIDTH) // 1
canvas_h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT) // 1

canvas = Canvas(window, width = canvas_w, height = canvas_h, bg = "red")
canvas.pack()

bw = 1

def handleBW():
    global bw
    bw = 1 - bw


button = Button(window, text= "Detection", command= handleBW)
button.pack()

photo = None

def update_frame():

    global canvas, photo, bw
    START_TIME = time.time()
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, dsize = None, fx = 1, fy = 1)
    
    if bw == 0:      
        cv2.imwrite("images\ " + "123" + ".jpg", cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))    
        time.sleep (0.5)
        bw = 1
        de.detection()
    else:
        frame

    photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
    
    canvas.create_image(0,0, image = photo, anchor = tkinter.NW)
    window.after(15, update_frame)

update_frame()

window.mainloop()