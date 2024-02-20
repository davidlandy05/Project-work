import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
 
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.open()

cred = credentials.Certificate("C:/Users/David Cummins/Downloads/david-6d9f5-firebase-adminsdk-y5nwf-40b213a236.json")
firebase_admin.initialize_app(cred,{'https://leaving-cert-project-9a808-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference()

while True:
    mb_one = str(ser.readline().decode('utf-8'))
    print(mb_one)
    mb_one = mb_one.replace(" ","")
    mb_one = mb_one.replace("\r\n","")
    print("You have walked "+mb_one)
    
    
    
    