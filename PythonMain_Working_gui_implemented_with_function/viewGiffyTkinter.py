import tkinter as tk
from PIL import Image

root = tk.Tk()
file="ambulance_scene_low.gif"

info = Image.open(file)

frames = info.n_frames  # gives total number of frames that gif contains

# creating list of PhotoImage objects for each frames
im = [tk.PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]

count = 0
anim = None
def animation(count):
    global anim
    im2 = im[count]

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    # globals()["anim"] = 
    anim = root.after(50,lambda :animation(count))

def stop_animation():
    root.after_cancel(anim)

try:
    if gif_label in root.winfo_children() : print("yess")
except :
    print("noo")

gif_label = tk.Label(root,image="")
gif_label.pack()

start = tk.Button(root,text="start",command=lambda :animation(count))
start.pack()

stop = tk.Button(root,text="stop",command=stop_animation)
stop.pack()

try:
    if gif_label in root.winfo_children() : print("yess")
except :
    print("noo")
    
root.mainloop()
