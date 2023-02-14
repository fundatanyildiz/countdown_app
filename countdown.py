from tkinter import *

root = Tk()
root.geometry('300x250')
root.title('Countdown')

widget_lbl = Label(root, font=('Arial', 18), text='Enter time in seconds!')
widget_lbl.pack(padx=20, pady=10)
widget = Entry(root, font=('Arial', 24, 'bold'),
               background='white', foreground='black')
widget.pack(padx=20, pady=10)


def submit():
    time_sec = widget.get()
    seconds = int(time_sec)
    countdown(seconds)


def countdown(seconds):
    mins, secs = divmod(seconds, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    lbl.config(text=timer)
    if seconds > 0:
        lbl.after(1000, countdown, seconds - 1)
    else:
        lbl.config(text='Time is up!')


button = Button(root, font=('Arial', 24, 'bold'),
                text='Start', command=submit)
button.pack(padx=20, pady=10)
lbl = Label(root, font=('Arial', 24, 'bold'), foreground='black')
lbl.pack(padx=20, pady=10)
mainloop()
