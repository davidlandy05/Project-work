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
counter1=0
counter2=0
counter3=0
variables = {}

for key,value in data.items():
    sleepy=int((value["You slept"]))
    sleep.append(sleepy)
    slept=sum(sleep)
    counter1=counter1+1
    Nslept=slept/counter1
    Nslept=math.floor(Nslept)
    
    

    
    works=int((value["Hours worked"]))
    worked.append(works)
    works=sum(worked)
    counter2=counter2+1
    Nwork=works/counter2
    Nwork=math.floor(Nwork)


    
    steps=int((value["Steps ran"]))
    steps=steps/2
    walked.append(steps)
    steped=sum(walked)
    steped=math.floor(steped)
    counter3=counter3+1
    Nsteped=steped/counter3
    Nsteped=math.floor(Nsteped)
    
   
    
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
    Nmood=moody/counter
    Nmood=math.floor(Nmood)
    variables[f'day{counter}'] = {
        'slept': sleepy,
        'works': works,
        'steped': steps,
        'moody': moody
    }


    
#These are averages
#print(slept)        
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

#Difference_slept=highest_slept-lowest_slept
#Difference_mood=mood_from_highest_slept-mood_from_lowest_slept
#Difference_works=works_from_highest_slept-works_from_lowest_slept
    
#Difference_exercise=highest_steped-lowest_steped
#Difference_mood2=mood_from_highest_steped-mood_from_lowest_steped
#Difference_slept2=slept_from_highest_steped-slept_from_lowest_steped
    


#print("When your sleep increased by",Difference_slept,"hours you mood increased by",Difference_mood,"units")
#print("When your sleep increased by",Difference_slept,"hours you productivity increased by",Difference_works,"hours")
#print("When your exercise increased by",Difference_exercise,"steps your sleep  increased by",Difference_mood,"hours")
#print("When your excercise increased by",Difference_exercise,"steps your mood increased by",Difference_works,"units")




well=""
mood1=mood_from_highest_slept
mood1=int(mood1)
if mood1==0:
    well=well+"forget to register"
elif mood1==1:
    well=well+"very sad"
elif mood1==2:
    well=well+"sad"
elif mood1==3:
    well=well+"okay"
elif mood1==4:
    well=well+"happy"
elif mood1==5:
    well=well+"very happy"
    
well2=""
mood2=mood_from_lowest_slept
mood2=int(mood2)
if mood2==0:
    well2=well2+"forget to register"
elif mood2==1:
    well2=well2+"very sad"
elif mood2==2:
    well2=well2+"sad"
elif mood2==3:
    well2=well2+"okay"
elif mood2==4:
    well2=well2+"happy"
elif mood2==5:
    well2=well2+"very happy"





def reccomendation(slept,highest_slept,lowest_slept,well,well2,works_from_highest_slept,works_from_lowest_slept):
    Rcounter=0
    recommend=[]
    Difference_slept=highest_slept-lowest_slept
    Difference_works=works_from_highest_slept-works_from_lowest_slept
    print("When your sleep increased by",Difference_slept,"hours you mood increased to",well,"from",well2)
    print("When your sleep increased by",Difference_slept,"hours you productivity increased by",Difference_works,"hours")
    if slept<8:
        better=8-slept
        Rcounter=Rcounter+1
        recommend.append("You are not getting the recommend hour of sleep.From this info we predict you will experince worse moods and a fall in productiveness")
    else:
        recommend.append("You are getting the recommend hours of sleep.From this info we predict tht if this habit is mantained,You will continue to have a good mood and continue to be productive")
        better=0
    
    return recommend, better, Rcounter,Difference_slept,well,Difference_works,well2

recommend, better, Rcounter,Difference_slept,well,well2,Difference_works =reccomendation(slept,highest_slept,lowest_slept,well,well2,works_from_highest_slept,works_from_lowest_slept)


print(recommend)

if Rcounter==1:
    print("We recommend getting",better,"more hours sleep to reach the reccomend 8 hours")
else:
    print("Well done you are getting the reccomend amount of hours of sleep!")
    
    
well3=""
mood3=mood_from_highest_slept
mood3=int(mood3)
if mood3==0:
    well3=well3+"forget to register"
elif mood3==1:
     well3=well3+"very sad"
elif mood3==2:
    well3=well3+"sad"
elif mood3==3:
    well3=well3+"okay"
elif mood3==4:
    well3=well3+"happy"
elif mood3==5:
    well3=well3+"very happy"
    
well4=""
mood4=mood_from_lowest_slept
mood4=int(mood4)
if mood4==0:
    well4=well4+"forget to register"
elif mood4==1:
     well4=well4+"very sad"
elif mood4==2:
    well4=well4+"sad"
elif mood4==3:
    well4=well4+"okay"
elif mood4==4:
    well4=well4+"happy"
elif mood4==5:
    well4=well4+"very happy"    
    
    
    
def reccomendation2(steped,highest_steped,lowest_steped,slept_from_highest_steped,slept_from_lowest_steped,well3,well4):
    recommend2=[]
    R2counter=0
    Difference_exercise=highest_steped-lowest_steped
    Difference_slept2=slept_from_highest_steped-slept_from_lowest_steped
    print("When your exercise increased by",Difference_exercise,"steps your sleep  increased to",well3,"from",well4)
    print("When your excercise increased by",Difference_exercise,"steps your mood increased by",Difference_slept2,"units")
    if steped<10:
        better2=10-steped
        R2counter=R2counter+1
        recommend2.append("You are not getting the recommend amount of steps.From this info the system predicts you will experince fatigue and a worsen mood")
    else:
        recommend2.append("You are getting the recommend amount of steps.From this info the system predicts that if this habit is mantained,You will continue to have better hours of sleep and continue to have an improved moods")
        better2=0
        R2counter=0
    return recommend2, better2, R2counter, Difference_slept2, Difference_exercise

recommend2, better2, R2counter,  Difference_slept2, Difference_exercise = reccomendation2(steped,highest_slept,lowest_slept,slept_from_highest_steped,slept_from_lowest_steped,well3,well4)

print(recommend2)

if R2counter==1:
    print("The system recommend getting",better2,"thousand more steps to reach the reccomend 10000")
else:
    print("Well done you are getting the recommend amount of steps!")
    
print(Nsteped)
print(Nwork)
print(Nmood)
print(Nslept)

objects = ('hours of sleep,work,wellbeing,steps(divided by 1000)')
y_pos = [0,1,2,3]
performance = [Nslept,Nwork,Nsteped,Nmood]

plt.bar(y_pos, performance, align='center', alpha=0.5)

plt.ylabel('Hours/steps (divided by 1000)')
plt.xlabel('hours of sleep,work,wellbeing,steps(divided by 1000)')
plt.title('Your average wellbeing stats per day')

plt.show()
