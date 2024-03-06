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
    works=math.floor(works)


    
    steps=int((value["Steps ran"]))
    steps=steps/2
    walked.append(steps)
    steped=sum(walked)
    steped=math.floor(steped)
   
    
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


    
#These are averages
print(slept)        
#print(works)        
#print(steped)    
#print(moody)

#This is all data stored by day
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

mood_from_highest_steped = variables[highest_steped_key]['moody']
slept_from_highest_steped = variables[highest_steped_key]['slept']
mood_from_lowest_steped = variables[lowest_steped_key]['moody']
slept_from_lowest_steped = variables[lowest_steped_key]['slept']

 


#print(f"Highest Slept: {highest_slept} (from variable {highest_slept_key})")
#print(f"Lowest Slept: {lowest_slept} (from variable {lowest_slept_key})")
#print(f"Highest Steped: {highest_steped} (from variable {highest_steped_key})")
#print(f"Lowest Steped: {lowest_steped} (from variable {lowest_steped_key})")
#print(f"Mood value from the variable with the highest Slept: {mood_from_highest_slept}")
#print(f"Works value from the variable with the highest Slept: {works_from_highest_slept}")
#print(f"Mood value from the variable with the lowest Slept: {mood_from_lowest_slept}")
#print(f"Works value from the variable with the lowest Slept: {works_from_lowest_slept}")

Difference_slept=highest_slept-lowest_slept
Difference_mood=mood_from_highest_slept-mood_from_lowest_slept
Difference_works=works_from_highest_slept-works_from_lowest_slept
    
Difference_exercise=highest_steped-lowest_steped
Difference_mood2=mood_from_highest_steped-mood_from_lowest_steped
Difference_slept2=slept_from_highest_steped-slept_from_lowest_steped
    


print("When your sleep increased by",Difference_slept,"hours you mood increased by",Difference_mood,"units")
print("When your sleep increased by",Difference_slept,"hours you productivity increased by",Difference_works,"hours")
print("When your exercise increased by",Difference_exercise,"steps your sleep  increased by",Difference_mood,"hours")
print("When your excercise increased by",Difference_exercise,"steps your mood increased by",Difference_works,"units")






plt.show()

def reccomendation(slept):
    Rcounter=0
    recommend=[]
    if slept<8:
        better=8-slept
        Rcounter=Rcounter+1
        recommend.append("You are not getting the recommend hour of sleep.From this info we predict you will experince worse moods and a fall in productiveness")
    else:
        recommend.append("You are getting the recommend hours of sleep.From this info we predict tht if this habit is mantained,You will continue to have a good mood and continue to be productive")
        better=0
    
    return recommend, better, Rcounter

recommend, better, Rcounter = reccomendation(slept)


print(recommend)

if Rcounter==1:
    print("We recommend getting",better,"more hours sleep to reach the reccomend 8 hours")
else:
    print("Well done you are getting the reccomend amount of hours of sleep!")
    
def reccomendation2(steped):
    R2counter=0
    recommend2=[]
    if steped<10:
        better2=10-steped
        R2counter=R2counter+1
        recommend2.append("You are not getting the recommend amount of steps.From this info we predict you will experince fatigue and a worsen mood")
    else:
        recommend2.append("You are getting the recommend amount of steps.From this info we predict that if this habit is mantained,You will continue to have better hours of sleep and continue to have an improved moods")
        better2=0
    
    return recommend2, better2, R2counter

recommend2, better2, R2counter = reccomendation2(steped)


print(recommend2)

if R2counter==1:
    print("We recommend getting",better2,"thousand more steps to reach the reccomend 10000")
else:
    print("Well done you are getting the reccomend amount of steps!")
    
    
objects = ('hours of sleep,work,wellbeing,steps(divided by 1000)')
y_pos = [0,1,2,3]
performance = [slept,works,steped,moody]

plt.bar(y_pos, performance, align='center', alpha=0.5)

plt.ylabel('Hours/steps (divided by 1000)')
plt.xlabel('hours of sleep,work,wellbeing,steps(divided by 1000)')
plt.title('Your wellbeing')

plt.show()
