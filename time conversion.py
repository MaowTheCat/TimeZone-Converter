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
    elif timezone1 == "EST":
        if timezone2 == "GMT":
            gmttimeest = int(time1)+4
            if gmttimeest > 24:
                gmttimeest = gmttimeest-24
            elif gmttimeest < 1:
                gmttimeest = gmttimeest+24
            time2.config(text=gmttimeest)
        elif timezone2 == "AEST":
            aesttimeest = int(time1)+14
            if aesttimeest > 24:
                aesttimeest = aesttimeest-24
            elif aesttimeest < 1:
                aesttimeest = aesttimeest+24
            time2.config(text=aesttimeest)
        elif timezone2 == "BST":
            bsttimeest = int(time1)+5
            if bsttimeest > 24:
                bsttimeest = bsttimeest-24
            elif bsttimeest < 1:
                bsttimeest = bsttimeest+24
            time2.config(text=bsttimeest)
    elif timezone1 == "AEST":
        if timezone2 == "GMT":
            gmttimeaest = int(time1)-10
            if gmttimeaest > 24:
                gmttimeaest = gmttimeaest-24
            elif gmttimeaest < 1:
                gmttimeaest = gmttimeaest+24
            time2.config(text=gmttimeaest)
        elif timezone2 == "EST":
            esttimeaest = int(time1)+14
            if esttimeaest > 24:
                esttimeaest = esttimeaest-24
            elif esttimeaest < 1:
                esttimeaest = esttimeaest+24
            time2.config(text=esttimeaest)
        elif timezone2 == "BST":
            bsttimeaest = int(time1)+9
            if bsttimeaest > 24:
                bsttimeaest = bsttimeaest-24
            elif bsttimeaest < 1:
                bsttimeaest = bsttimeaest+24
            time2.config(text=bsttimeaest)
    elif timezone1 == "BST":
        if timezone2 == "GMT":
            gmttimebst = int(time1)-1
            if gmttimebst > 24:
                gmttimebst = gmttimebst-24
            elif gmttimebst < 1:
                gmttimebst = gmttimebst+24
            time2.config(text=gmttimebst)
        elif timezone2 == "EST":
            esttimebst = int(time1)-5
            if esttimebst > 24:
                esttimebst = esttimebst-24
            elif esttimebst < 1:
                esttimebst = esttimebst+24
            time2.config(text=esttimebst)
        elif timezone2 == "AEST":
            aesttimebst = int(time1)+9
            if aesttimebst > 24:
                aesttimebst = aesttimebst-24
            elif aesttimebst < 1:
                aesttimebst = aesttimebst+24
            time2.config(text=aesttimebst)
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