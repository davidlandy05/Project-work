import serial
import time
 
ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM4"
ser.open()
 
while True:
    mb_one = str(ser.readline().decode('utf-8'))
    print(mb_one)
    mb_one = mb_one.replace(" ","")
    mb_one = mb_one.replace("\r\n","")
    print(mb_one)
    
    
    
    