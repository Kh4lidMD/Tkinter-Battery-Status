from tkinter import *
from psutil import sensors_battery
from time import sleep

window = Tk()
window.title("Battery Status")
window.geometry("300x300")
window.config(bg='black')
window.iconphoto(False, PhotoImage(file='icon.png'))
def get_percentage():
    return sensors_battery().percent

header = Label(
    window, text="Battery Status", 
    anchor="center", pady=50, 
    fg='white', bg='black', 
    font=10)
header.pack()

percent =  Label(
    window, text="Here is the percentage", 
    font=7, anchor="center",
    fg='green', bg='black')
percent.pack()

is_plugged = Label(
    window, text='Is Plugged',
    font=7, anchor="center",
    bg='black')

def recheck_power():
    if sensors_battery().power_plugged:
        is_plugged.config(fg='green')
        is_plugged.config(text='Plugged')
    else:
        is_plugged.config(fg='red')
        is_plugged.config(text='Not Plugged')

def recheck_percent():
    color = ''
    result = sensors_battery().percent
    if result >= 50:
        color = 'green'
    elif result < 50:
        color = 'yellow'
    elif result < 20:
        color = 'red'
    percent.config(fg=color, text=f'{result}%')

recheck_percent()
recheck_power()

is_plugged.pack()

window.mainloop()
