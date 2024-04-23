import  tkinter
from  tkinter import *
import pyshorteners

root = Tk()
root.title("URL Shortener")
root.geometry("330x450")
root.config(background="#DC143C")

def url_shortener():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url.get())
    short_url_en.insert(0,short_url)


heading = Label(root,text="Enter Long URL: ",font=("Arial",11,"bold"),bg="#DC143C",fg="Black")
heading.pack(pady=(30,0))

long_url = Entry(justify="center",width=31,font=("poppins",12),bg="white",border=2)
long_url.pack(pady=20)
long_url.focus()

heading = Label(root,text="Your Shortened URL: ",font=("Arial",11,"bold"),bg="#DC143C",fg="Black")
heading.pack(pady=(10,0))

short_url_en = Entry(justify="center",width=31,font=("poppins",12),bg="white",border=2)
short_url_en.pack(pady=20)
short_url_en.focus()

btn = Button(root,text="Shorten URL",bg="red",fg="white",font=("arial",12,"bold"),command=url_shortener)
btn.pack(pady=13)

root.mainloop()

