import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
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
variables = {}

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
    
    variables[f'day{counter}'] = {
        'slept': sleepy,
        'works': works,
        'steped': steps,
        'moody': moody
    }

print(slept)        
print(works)        
print(steped)    
print(moody)
print(variables)

lowest_steped = float('inf')
highest_steped = float('-inf')
lowest_slept = float('inf')
highest_slept = float('-inf')

for key, value in variables.items():
        
    if value['slept'] < lowest_slept:
        lowest_slept = value['slept']
        lowest_slept_key = key
    if value['slept'] > highest_slept:
        highest_slept = value['slept']
        highest_slept_key = key

    if value['steped'] < lowest_steped:
        lowest_steped = value['steped']
        lowest_steped_key = key
    if value['steped'] > highest_steped:
        highest_steped = value['steped']
        highest_steped_key = key

mood_from_highest_slept = variables[highest_slept_key]['moody']
works_from_highest_slept = variables[highest_slept_key]['works']
mood_from_lowest_slept = variables[lowest_slept_key]['moody']
works_from_lowest_slept = variables[lowest_slept_key]['works']

 


#print(f"Highest Slept: {highest_slept} (from variable {highest_slept_key})")
#print(f"Lowest Slept: {lowest_slept} (from variable {lowest_slept_key})")
#print(f"Highest Steped: {highest_steped} (from variable {highest_steped_key})")
#print(f"Lowest Steped: {lowest_steped} (from variable {lowest_steped_key})")
#print(f"Mood value from the variable with the highest Slept: {mood_from_highest_slept}")
#print(f"Works value from the variable with the highest Slept: {works_from_highest_slept}")
#print(f"Mood value from the variable with the lowest Slept: {mood_from_lowest_slept}")
#print(f"Works value from the variable with the lowest Slept: {works_from_lowest_slept}")
def find_difference(highest_slept,lowest_stept,mood_from_highest_slept,mood_from_lowest_slept,works_from_highest_slept,works_from_lowest_slept):
    Difference_slept=highest_slept-lowest_slept
    Difference_mood=mood_from_highest_slept-mood_from_lowest_slept
    Difference_works=works_from_highest_slept-works_from_lowest_slept
    


print("When your sleep increased by",Difference_slept,"hours you mood increased by",Difference_mood,"units")
print("When your sleep increased by",Difference_slept,"hours you productivity increased by",Difference_works,"hours")




#objects = ('hours of sleep,work,wellbeing,steps(divided by 1000)')
#y_pos = [0,1,2,3]
#performance = [slept,works,steped,moody]

#plt.bar(y_pos, performance, align='center', alpha=0.5)

#plt.ylabel('Hours/steps (divided by 1000)')
#plt.xlabel('hours of sleep,work,wellbeing,steps(divided by 1000)')
#plt.title('Your wellbeing')

#plt.show()
    
