'''
The Time complexity of this program in worst case is O(n).
The space complexity of this program in worst case is O(1).
'''


import tkinter as tk
from tkinter import *
import time

root = tk.Tk()
root.resizable(width=0,height=0)
root.geometry("400x170+200+100")

# To display the time
def myTime():
    timeStr = time.strftime("%I:%M:%S")
    displayTime.config(text=timeStr)
    displayTime.after(1000,myTime)
            
    
            
# Show alarm container            
def alarmReached():
    screen = tk.Toplevel()
    screen.resizable(width=0,height=0)
    screen.geometry("300x200")
    lbl = tk.Label(screen,text="Alarm")
    lbl.grid(row=0,column=1,padx=5,pady=5)
    
    #snooze and dismiss
    def snooze():
        time.sleep(3)   
    def dismiss():
        screen.destroy()    
    
    snoozeBtn = tk.Button(screen,text="Snooze",command=snooze)
    snoozeBtn.grid(row=1,column=1,padx=5,pady=5)
    dissmissBtn = tk.Button(screen,text="Dismiss",command=dismiss)
    dissmissBtn.grid(row=1,column=2,padx=5,pady=5)
            
# show to alarm on the view
def showAlarm(alarmtime):
    x = time.strftime("%H:%M:%S").split(":")
    timeString = alarmtime.split(":")
    shownOnGrid = tk.Label(root,text=alarmtime)
    shownOnGrid.grid(row=2,column=0,padx=5,pady=25)
    
    # To delete the alarm from grid
    def deleteAlarm():
        shownOnGrid.destroy()
        alarmDelete.destroy()
    
    alarmDelete = tk.Button(root,text="Delete",command=deleteAlarm)
    alarmDelete.grid(row=2,column=2,padx=5,pady=25)
    while((x[0]>= timeString[0] ) and (x[1]!= timeString[1])):
        x = time.strftime("%I:%M:%S").split(":")
    if((timeString[0] == x[0])or (timeString[1] == x[1])):
        shownOnGrid.destroy()
        alarmDelete.destroy()
        alarmReached() 

# To add an Alarm
def addAlarm():
    top = tk.Toplevel()
    top.resizable(width=0,height=0)
    top.geometry("300x200")
    textLable = tk.Label(top,text="Time (hh:mm): ").grid(row=0,column=0,padx=5,pady=5)
    alarmTillEntry = tk.Entry(top,borderwidth=4)
    alarmTillEntry.grid(row=0,column=1,padx=5,pady=5)
    
    # To show the time on the lable
    def clickBtn():
        showAlarm(alarmTillEntry.get())
        top.destroy()
        
    addAlarmBtn = tk.Button(top,command=clickBtn,text="add").grid(row=1,column=1,padx=5,pady=5)
    

timeLabel = tk.Label(text="Current Time: ").grid(row=0,column=0,padx=5,pady=25)
displayTime = tk.Label()
displayTime.grid(row=0,column=2,pady=25,padx=5)
addAlarm = tk.Button(text="Add Alarm",command=addAlarm).grid(row=1,column=1)
myTime()
root.mainloop()
