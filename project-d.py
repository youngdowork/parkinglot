import datetime
from flask import Flask, render_template, Response
from PIL import Image
import serial
import sys
import time
#import datetime.datetime

 
a_entrtime = None
b_entrtime = None
c_entrtime = None
a_exittime = None
b_exittime = None
c_exittime = None
a_parktime = None
b_parktime = None
c_parktime = None
a_cost = None
b_cost = None
c_cost = None
a_subsec = 0
b_subsec = 0
c_subsec = 0


ard = serial.Serial('COM3',9600)
 
app = Flask(__name__)
 
@app.route('/parkinglot',methods=['GET','POST'])
 
def parkinglot():
    a_var= ard.readline().decode()
    b_var= ard.readline().decode()
    c_var= ard.readline().decode()
    d_var= ard.readline().decode()

    global a_entrtime
    global b_entrtime
    global c_entrtime
    global a_exittime
    global b_exittime
    global c_exittime
    global a_parktime
    global b_parktime
    global c_parktime
    global a_cost
    global b_cost
    global c_cost
    global a_subsec
    global b_subsec
    global c_subsec

        
    a = int(a_var)
    b = int(b_var)
    c = int(c_var)
    d = int(d_var)

    if a==1 and a_entrtime==None: 
        a_entrtime = datetime.datetime.now()
        print(a_entrtime)

    if b==1 and b_entrtime==None:
        b_entrtime = datetime.datetime.now()
        print(b_entrtime)
 
    if c==1 and c_entrtime==None: 
        c_entrtime = datetime.datetime.now()
        print(c_entrtime)

################################################






    if a==0 and a_entrtime!=None:
        a_exittime = datetime.datetime.now()
        a_subsec = 0
        a_entrsec = int(a_entrtime.strftime('%S'))
        a_exitsec = int(a_exittime.strftime('%S'))
        if a_exitsec >= a_entrsec :
            a_subsec = a_exitsec - a_entrsec
        else :
            a_subsec = a_exitsec+60 - a_entrsec
        a_entrtime = None
    elif a==0 and a_entrtime==None:
        a_subsec = 0

    if b==0 and b_entrtime!=None:
        b_exittime = datetime.datetime.now()
        b_subsec = 0
        b_entrsec = int(b_entrtime.strftime('%S'))
        b_exitsec = int(b_exittime.strftime('%S'))
        if b_exitsec >= b_entrsec :
            b_subsec = b_exitsec - b_entrsec
        else :
            b_subsec = b_exitsec+60 - b_entrsec
        b_entrtime = None
    elif b==0 and b_entrtime==None:
        b_subsec = 0

    if c==0 and c_entrtime!=None:
        c_exittime = datetime.datetime.now()
        c_subsec = 0
        c_entrsec = int(c_entrtime.strftime('%S'))
        c_exitsec = int(c_exittime.strftime('%S'))
        if c_exitsec >= c_entrsec :
            c_subsec = c_exitsec - c_entrsec
        else :
            c_subsec = c_exitsec+60 - c_entrsec
        c_entrtime = None
    elif c==0 and c_entrtime==None:
        c_subsec = 0
        




    a = str(a)
    b = str(b)
    c = str(c)
    d = str(d)

    return render_template('project-b.html', d_var=d_var, a=a, b=b, c=c, a_subsec=a_subsec, b_subsec=b_subsec, c_subsec=c_subsec,  image_file1="image/"+a+".jpg",image_file2="image/"+b+".jpg",image_file3="image/"+c+".jpg")


 
app.run('0.0.0.0',port = 80)