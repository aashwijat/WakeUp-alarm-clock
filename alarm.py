import customtkinter as ctk
import datetime
import winsound
import time

## set alarm function
def set_alarm(alarm_time):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Set Date is :",date)
        print(now)
        if now == alarm_time:
            print("Time to wake up")
            winsound.PlaySound("dynamite.mp3",winsound.SND_ASYNC)
        break
def actual_time():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    set_alarm(alarm_time)

## creating GUI

root = ctk.CTk()
root.title("alarm clock")
root.geometry("680x350")

#setting appearence mode of app
ctk.set_appearance_mode("system")

#setting theme
ctk.set_default_color_theme("dark-blue")

## widgets
time_format = ctk.CTkLabel(root,text="Enter time in 24h format!", font=("helvetica",16,"bold")).grid(row=1,column=6,padx=20,pady=20,sticky="e")
#time_format.place(x=60,y=120)
add_time = ctk.CTkLabel(root, text="Hour",font=("helvetica",60,"bold")).grid(row=3,column=2,padx=20,pady=10)
add_time1 = ctk.CTkLabel(root, text="Minute",font=("helvetica",60,"bold")).grid(row=3,column=6,padx=20,pady=20)
add_time2 = ctk.CTkLabel(root, text="Second",font=("helvetica",60,"bold")).grid(row=3,column=10,padx=20,pady=10)
#add_time.place(x=110)
#setAlarm = ctk.CTkLabel(root, text="When to wake up?",font=("helvetica",10,"bold")).grid(row=1,column=1)
#.place(x=0,y=29)

hour = ctk.StringVar()
minute = ctk.StringVar()
second = ctk.StringVar()

hourTime = ctk.CTkEntry(root,textvariable=hour,width=100,height=50).grid(row=5,column=2)#.place(x=100,y=30)
minTime = ctk.CTkEntry(root,textvariable=minute,width=100,height=50).grid(row=5,column=6)#.place(x=150,y=30)
secTime = ctk.CTkEntry(root,textvariable=second,width=100,height=50).grid(row=5,column=10)#.place(x=200,y=30)

submit = ctk.CTkButton(root, text="Set Alarm",width=20, height=40 ,command=actual_time).grid(row=20,column=6,padx=40,pady=40,sticky="nsew")#.place(x=110,y=70)

root.mainloop()


