# 1. Calorie Counter: Write a program that asks the user for their 
#age, weight, and activity level, then calculates their daily 
#calorie goal based on recommended guidelines. Use if-else statements to adjust the goal based on the user's activity 
#level
recommend={}
for i in range(3):
    recommend__level=input("Activity level: ").lower()
    recommend_calorie=input("Calories: ")
    recommend[recommend__level]=recommend_calorie

age=int(input("Age: "))
weight=int(input("Weight: "))
activity_level=input("Activity level (High, low, moderate): ").lower()

for key, values in recommend.items():
    if key==activity_level:
        print("Calorie goal",values)




#2. Sleep Tracker: Create a program that asks the user for their 
#bedtime and wake-up time, then calculates their total sleep 
#duration. Use if statements to determine if they met the recommended sleep amount and 
#provide feedback accordingly.
recommend_sleep=int(input("Recommend Sleep amount: ").replace("hour",""))
bedtime=int(input("Bed Time (Pm): ").replace("pm",""))
wakeup=int(input("Wakeup Time (am): ").replace("am",""))
time_list=[]
for i in range(bedtime,12+1):
    time_list.append(i)


for i in range(1,wakeup+1):
    time_list.append(i)
time=len(time_list)
print(time)

if time>recommend_sleep:
    time_waste=time-recommend_sleep
    print(f"You slept {time_waste} hours more than recommend (Recommend Hours {recommend_sleep}) ")
elif time<recommend_sleep:
    time_waste=recommend_sleep-time
    print(f"You slept {time_waste} hours less than recommend (Recommend Hours {recommend_sleep})")
else:
    print(f"Congratulations, you slept exactly as much as you had said (Recommend Hours {recommend_sleep})")




#3. Hydration Helper: Design a program that prompts the user for their weight and desired level of 
#hydration (e.g., light, moderate, intense exercise). Use nested if-else statements to suggest the 
#amount of water they should drink throughout the day
weight=int(input("Weight: "))
hydration_level=input("Hydration level: ").lower()
while True:
    if weight<30 and weight>100:
        print("Weight must be grater than 30 and less than 100")
        y_n=input("Do you want to continue(y or n): ")
        if y_n=="n":
            break
    else:
        
            if weight>=30 and weight<55:
                if hydration_level=="light":
                    water=weight*26
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                elif hydration_level=="moderate":
                    water=weight*28
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                elif hydration_level=="intense exercise":
                    water=weight*30
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                else:
                    print("Hydration desired level (Light,Moderate,Intense Exercise)")
                    y_n=input("Do you want to Continue? (y or n): ").lower()
                    if y_n=="n":
                        break
            elif weight>=55 and weight<70:
                if hydration_level=="light":
                    water=weight*30
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                elif hydration_level=="moderate":
                    water=weight*32
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                elif hydration_level=="Intense exercise":
                    water=weight*35
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                else:
                    print("Hydration desired level (Light,Moderate,Intense Exercise)")
                    y_n=input("Do you want to Continue? (y or n): ").lower()
                    if y_n=="n":
                        break
            elif weight>=70 and weight<=100:
                if hydration_level=="light":
                    water=weight*36
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                elif hydration_level=="moderate":
                    water=weight*38
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                elif hydration_level=="Intense exercise":
                    water=weight*40
                    print(f"To achieve your desired hydration level, you need to drink {water}ml of water throughout the day")
                    break
                else:
                    print("Hydration desired level (Light,Moderate,Intense Exercise)")
                    y_n=input("Do you want to Continue? (y or n): ").lower()
                    if y_n=="n":
                        break

print("Thanks")

