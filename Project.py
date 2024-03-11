import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
 
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.open()

cred = credentials.Certificate("C:/Users/18DLandy.ACC/Downloads/leaving-cert-project-9a808-firebase-adminsdk-xb3od-0797d54160.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://leaving-cert-project-9a808-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference()
#ref.update({'Steps ran':''})
ref = db.reference().child('Steps ran')
hours_of_sleep = 0
work =1
wellbeing =2
steps = 3
while True:
    mb_one = str(ser.readline().decode('utf-8'))
    print(repr(mb_one.strip()))
    data_in =mb_one.strip().split(',')
    
    print(data_in[steps])
    print(data_in[work])
    print(data_in[wellbeing])
    print(data_in[hours_of_sleep])


    counter=0
    well=""
    mood=data_in[wellbeing]
    mood=int(mood)
    if mood==0:
        well=well+"forget to register"
    elif mood==1:
        well=well+"very sad"
    elif mood==2:
        well=well+"sad"
    elif mood==3:
        well=well+"okay"
    elif mood==4:
        well=well+"happy"
    elif mood==5:
        well=well+"very happy"
    counter=counter+1
    mood=mood/counter

    
    mb_one = mb_one.replace(" ","")
    mb_one = mb_one.replace("\r\n","")
    ref.update({str(int(time.time())):{'Steps ran':(data_in[steps]),"Hours worked":(data_in[work]),"Your wellbeing is":well,"You slept":(data_in[hours_of_sleep])}})
    
 
    

    
    