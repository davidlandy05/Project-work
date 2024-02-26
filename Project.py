import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
 
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

cred = credentials.Certificate("C:/Users/18DLandy.ACC/Downloads/leaving-cert-project-9a808-firebase-adminsdk-xb3od-0192c6e1b1.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://leaving-cert-project-9a808-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference()
ref.update({'Steps ran':''})
ref = db.reference().child('Steps ran')

while True:
    mb_one = str(ser.readline().decode('utf-8'))
    print(mb_one)
    mb_one = mb_one.replace(" ","")
    mb_one = mb_one.replace("\r\n","")
    print("You have walked ",mb_one," steps")
    ref.update({str(int(time.time())):{'Steps ran':mb_one}})
    
    
    
    