#Time Tracking: The program will keep track of the time of day.
#Loop for Multiple Meals: It will have a loop to handle multiple meals in a day.
#If-Else Statements: Depending on the time of day, the program will decide which meal is currently being planned.
#Dictionary for Diet Plan: The program will use a dictionary to store the diet plan for each meal.
from datetime import datetime

diet_plan = {
    'breakfast': ['Oatmeal', 'Banana', 'Milk'],
    'lunch': ['Grilled Chicken', 'Quinoa', 'Vegetables'],
    'snack': ['Greek Yogurt', 'Berries','Tea'],
    'dinner': ['Salmon', 'Sweet Potato', 'Broccoli']
}
    

current=datetime.now()
current_string=current.strftime("%I:%M")
current_hour=int(current.hour)

    
if current_hour<12 and current_hour>8:
    for key,values in diet_plan.items():
        if key=="breakfast":
            print("Breakfast Time")
            print(current_string)
            for i in values:
                print(i)
elif current_hour>12 and current_hour<14:
    for key,values in diet_plan.items():
        if key=="lunch":
            print("Lunch Time")
            print(current_string)
            for i in values:
                print(i)
elif current_hour>16 and current_hour<18:
    for key,values in diet_plan.items():
        if key=="snack":
            print("Snack Time")
            print(current_string)
            for i in values:
                print(i)
elif current_hour>21 and current_hour<22:
    for key,values in diet_plan.items():
        if key=="dinner":
            print("Dinner Time")
            print(current_string)
            for i in values:
                print(i)













