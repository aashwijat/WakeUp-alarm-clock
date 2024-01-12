import tkinter as tk
from tkinter import ttk
import datetime
import time
from playsound import playsound
import threading 

root = tk.Tk()
root.geometry("400x350")
root.config(bg="#2d174f")
root.title("alarm clock")


def Threading():
    t1 = threading.Thread(target=alarm, daemon=True)
    t1.start()

def alarm():
    while True:
        set_alarm = f"{hour.get()}:{minute.get()}:{seconds.get()}"

        time.sleep(1)

        current_time  = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time==set_alarm:
            text_label = tk.Label(root, text="wake up!", fg="#fffbb8", bg="#2d174f", font=("helvetica",14,"bold")).pack(pady=10)
            playsound("dynamite.mp3")
            break

## window

label = tk.Label(root, text="A L A R M", font=("helvetica",22,"bold"),bg="#2d174f", fg="#cdadff").pack(pady=10)

frame = tk.Frame(root)
frame.pack()
frame.config(bg="#2d174f")

frame1 = tk.Frame(root)
frame1.pack()
frame1.config(bg="#2d174f")

hour_label = tk.Label(frame, text="HOUR", font=("helvetica",16,"bold"),bg="#2d174f", fg="#fffbb8").pack(side="left", padx=20,pady=10)
min_label = tk.Label(frame, text="MINS", font=("helvetica",16,"bold"),bg="#2d174f", fg="#fffbb8").pack(side="left", padx=20,pady=10)
second_label = tk.Label(frame, text="SECS", font=("helvetica",16,"bold"),bg="#2d174f", fg="#fffbb8").pack(side="left", padx=20,pady=10)

## HOURS
hour = tk.StringVar(root)
hour_menu = ttk.Combobox(frame1, height=10, width=5,textvariable=hour)
hour_menu.pack(side='left',padx=20,pady=20)
hour_menu['values'] = ['00','01','02','03','04', '05', '06', '07',
         '08', '09', '10', '11', '12', '13', '14', '15',
         '16', '17', '18', '19', '20', '21', '22', '23']


## MINS
minute = tk.StringVar(root)
min_menu = ttk.Combobox(frame1,height=10,width=5, textvariable=minute)
min_menu.pack(side='left',padx=20,pady=20)
min_menu['values']=['00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59']

seconds = tk.StringVar(root)
sec_menu = ttk.Combobox(frame1,height=10, width=5,textvariable=seconds)
sec_menu.pack(side="left", padx=20,pady=20)
sec_menu['values']=['00', '01', '02', '03', '04', '05', '06', '07',
           '08', '09', '10', '11', '12', '13', '14', '15',
           '16', '17', '18', '19', '20', '21', '22', '23',
           '24', '25', '26', '27', '28', '29', '30', '31',
           '32', '33', '34', '35', '36', '37', '38', '39',
           '40', '41', '42', '43', '44', '45', '46', '47',
           '48', '49', '50', '51', '52', '53', '54', '55',
           '56', '57', '58', '59']


## label button
#text_label = tk.Label(root, text="wake up!", font=("helvetica",14,"bold"),bg="#2d174f", fg="#fffbb8").pack(pady=5)

## set button
set_btn = tk.Button(root, text="SET ALARM", font=("helvetica",16,"bold"), bg="#fffbb8", fg="#2d174f", command=Threading).pack(pady=10)


## stop button
stop_btn = tk.Button(root, text="STOP", font=("helvetica",16,"bold"), bg="#fffbb8", fg="#2d174f", command=exit).pack(pady=10)

root.mainloop()
