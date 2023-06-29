from pystray import MenuItem as item
import pystray
from PIL import Image
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

window = tk.Tk()
window.geometry("500x500")
window.resizable(False, False)
window.title("System Tray Demo")

def clickMe():
   showinfo(
        title='About',
        message='Button was clicked!'
    )

w = ttk.Button(window, text = "Click", command = clickMe)

w.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

def quit_window(icon, item):
    icon.stop()
    window.destroy()

def show_window(icon, item):
    icon.stop()
    window.after(0,window.deiconify)

def withdraw_window():  
    window.withdraw()
    image = Image.open("icon.png")
    menu = (item('Show', show_window), item('Quit', quit_window))
    icon = pystray.Icon("name", image, "title", menu)
    icon.run()

window.protocol('WM_DELETE_WINDOW', withdraw_window)
window.mainloop()
