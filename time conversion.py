# Made by Maow
# https://github.com/MaowTheCat
# This can only do it by the hour
# Example: 10 Non-Example: 10:00
# Don't go above 24
# If you get a negative result then subtract that by 24
# This uses 24 hour clock

from tkinter import *
from tkinter import messagebox

timezones = ("GMT", "EST", "AEST", "BST")

window = Tk()
window.title("Time conversion")
window.geometry('650x200')
window.tk.call('tk', 'scaling', 2.0)

def convert():
    timezone1 = spinnum1.get()
    timezone2 = spinnum2.get()
    time1 = time.get()
    time2 = Label(window, text="", width=9, font=("Ariel", 20))
    time2.grid(column=4, row=3)
    if timezone1 == timezone2:
        time2.config(text=time1)
    elif time1 == "":
        messagebox.showinfo(title="Error", message="That is not a valid time")
    elif timezone1 == "GMT":
        if timezone2 == "EST":
            esttimegmt = int(time1)-4
            if esttimegmt > 24:
                esttimegmt = esttimegmt-24
            elif esttimegmt < 1:
                esttimegmt = esttimegmt+24
            time2.config(text=esttimegmt)
        elif timezone2 == "AEST":
            aesttimegmt = int(time1)+10
            if aesttimegmt > 24:
                aesttimegmt = aesttimegmt-24
            elif aesttimegmt < 1:
                aesttimegmt = aesttimegmt+24
            time2.config(text=aesttimegmt)
        elif timezone2 == "BST":
            bsttimegmt = int(time1)+1
            if bsttimegmt > 24:
                bsttimegmt = bsttimegmt-24
            elif bsttimegmt < 1:
                bsttimegmt = bsttimegmt+24
            time2.config(text=bsttimegmt)
    else:
        messagebox.showinfo(title="Error", message="That is not a valid time")

lbl = Label(window, text="     ")
lbl.grid(column=0, row=0)

spinnum1 = Spinbox(window, values=timezones)
spinnum1.grid(column=2, row=2)

spacer = Label(window, text="  >  ")
spacer.grid(column=3, row= 2)

convertbtn = Button(window, text="Convert", command=convert)
convertbtn.grid(column=3, row=4)

spinnum2 = Spinbox(window, values=timezones)
spinnum2.grid(column=4, row=2)

time = Entry(window, width=9, font=("Ariel", 20))
time.grid(column=2, row=3)
time.get()

window.mainloop()