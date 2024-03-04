import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial
import matplotlib.pyplot as plt
import math



cred = credentials.Certificate("C:/Users/18DLandy.ACC/Downloads/leaving-cert-project-9a808-firebase-adminsdk-xb3od-0797d54160.json")
firebase_admin.initialize_app(cred,{'databaseURL':'https://leaving-cert-project-9a808-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference()
ref = db.reference().child('Steps ran')

data=ref.get()


sleep=[]
walked=[]
mood=[]
worked=[]
counter=0

for key,value in data.items():
    sleepy=int((value["You slept"]))
    sleep.append(sleepy)
    slept=sum(sleep)

    
    works=int((value["Hours worked"]))
    worked.append(works)
    works=sum(worked)


    
    steps=int((value["Steps ran"]))
    steps=steps/2
    walked.append(steps)
    steped=sum(walked)
   
    
    if (value['Your wellbeing is'])=="forget to register":
        wellbeing=0
        counter=counter+1
        fort=wellbeing/counter
        mood.append(fort)
    elif (value['Your wellbeing is'])=="very sad":
         wellbeing=1
         counter=counter+1
         fort=wellbeing/counter
         mood.append(fort)
    elif (value['Your wellbeing is'])=="sad":
         wellbeing=2
         counter=counter+1
         fort=wellbeing/counter
         mood.append(fort)
    elif (value['Your wellbeing is'])=="okay":
         wellbeing=3
         counter=counter+1
         fort=wellbeing/counter
         mood.append(fort)
    elif (value['Your wellbeing is'])=="happy":
         wellbeing=4
         counter=counter+1
         fort=wellbeing/counter
         mood.append(fort)
    elif (value['Your wellbeing is'])=="very happy":
         wellbeing=5
         counter=counter+1
         fort=wellbeing/counter
         mood.append(fort)
    moody=sum(mood)
    moody=math.floor(moody)
                                       
 

print(slept)        
print(works)        
print(steped)    
print(moody)


objects = ('hours of sleep,work,wellbeing,steps(divided by 1000)')
y_pos = [0,1,2,3]
performance = [slept,works,steped,moody]

plt.bar(y_pos, performance, align='center', alpha=0.5)

plt.ylabel('Hours/steps (divided by 1000)')
plt.xlabel('hours of sleep,work,wellbeing,steps(divided by 1000)')
plt.title('Your wellbeing')

plt.show()
    
