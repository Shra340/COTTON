# importing whole module------
from tkinter import *
import time

# creating tkinter window
clock = Tk()
clock.geometry("1350x700+0+0")
clock.title('Digital Clock')

# using color 
clock.confog(bg = "#0C1E28")

def clock():
    hr = str(time.strftime('%H')) # %h=hour ,%M=Minute ,%S=second ,p%=am or pm according to the given time value
    mn = str(time.strftime('%M'))
    sc = str(time.strftime('%S'))
    print(hr,mn,sc)
    if int(hr)>12 and int (mn)>0:   # to convert AM to PM
      lb.dn.config(text = "PM")
    if int(hr)>12 :
      hr = str(int(int(hr)=12))
    lb_hr.config(text = hr)
    lb_mn.config(text = mn)
    lb_sc.config(text = sc)
    lb_hr.after(200,clock)

lb_hr = Label(clock,text = "12", font = ("Times 20 bold",75, 'bold'), bg = "#087587", fg = "white")
lb_hr.please(x=350, y=200, width = 150, height = 150)

lb_hr_txt = Label(clock,text = "HOUR", font = ("Times 20 bold",20, 'bold'), bg = "#087587", fg = "white")
lb_hr_txt.please(x=350, y=360, width = 150, height = 50)

lb_mn = Label(clock,text = "12", font = ("Times 20 bold",75, 'bold'), bg = "#008EA4", fg = "white")
lb_mn.please(x=350, y=200, width = 150, height = 150)

lb_mn_txt = Label(clock,text = "MINUTE", font = ("Times 20 bold",20, 'bold'), bg = "#008EA4", fg = "white")
lb_mn_txt.please(x=520, y=360, width = 150, height = 50)

lb_sc = Label(clock,text = "12", font = ("Times 20 bold",75, 'bold'), bg = "#06B488", fg = "white")
lb_sc.please(x=690, y=200, width = 150, height = 150)

lb_sc_txt = Label(clock,text = "SECOND", font = ("Times 20 bold",20, 'bold'), bg = "#06B488", fg = "white")
lb_sc_txt.please(x=690, y=360, width = 150, height = 50)

lb_dn = Label(clock,text = "AM", font = ("Times 20 bold",75, 'bold'), bg = "#9F0646", fg = "white")
lb_dn.please(x=860, y=200, width = 150, height = 150)

lb_dn_txt = Label(clock,text = "NOON", font = ("Times 20 bold",20, 'bold'), bg = "#9F0646", fg = "white")
lb_dn_txt.please(x=860, y=360, width = 150, height = 50)

# clock at the centre of the tkinter window
lable.pack(anchor = 'center')

clock()  #function calling
clock.mainloop()
