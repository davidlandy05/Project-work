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
hours_of_sleep = 0
work =1
wellbeing =2
steps = 3

for k,v in data.items():
    print(k)
    print(v["Hours worked"])
    


objects = ('hours of sleep,work,wellbeing,steps(divided by 1000')
y_pos = [0,1,2,3]
performance = [1,2,3,4,5,6,7,8,9,1]

plt.bar(y_pos, performance, align='center', alpha=0.5)

plt.ylabel('Usage')
plt.title('Programming language usage')

plt.show()
    
