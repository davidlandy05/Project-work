import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import matplotlib.pyplot as plt



cred = credentials.Certificate("C:/Users/18DLandy.ACC/Downloads/leaving-cert-project-9a808-firebase-adminsdk-xb3od-0797d54160.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://leaving-cert-project-9a808-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference()
ref = db.reference().child('Steps ran')

data=ref.get()
print(data)

sleep=[]
walked=[]
mood=[]
worked=[]


for key,value in data.items():
    sleepy=int((value["You slept"]))
    sleep.append(sleepy)
    slept=sum(sleep)
    print(slept)
    
    works=int((value["Hours worked"]))
    worked.append(works)
    worked=sum(worked)
    print(worked)
    
    steps=int((value["Steps ran"]))
    steps=steps/2
    walked.append(steps)
    print(steps)
    
    if (Value['Your wellbeing is'])=="forget to register":
        mood=mood+0
    elif (Value['Your wellbeing is'])=="very sad":
        mood=mood+1
    elif (Value['Your wellbeing is'])=="sad":
        mood=mood+2
    elif (Value['Your wellbeing is'])=="okay":
        mood=mood+3
    elif (Value['Your wellbeing is'])=="happy":
        mood=mood+4
    elif (Value['Your wellbeing is'])=="very happy":
        mood=mood+5
    print(mood)    
        
        
 
    



#objects = ('hours of sleep,work,wellbeing,steps(divided by 1000')
#y_pos = [0,1,2,3]
#performance = []

#plt.bar(y_pos, performance, align='center', alpha=0.5)

#plt.ylabel('Usage')
#plt.title('Programming language usage')

#plt.show()
    
