#1. Write a Python program to check if a given number is positive, negative, or zero
num=int(input("Number: "))
if num>0:
    print("Positive")
elif num<0:
    print("Negative")
else:
    print("Zero")

#2. Create a program that asks the user to enter their age and prints out whether they are a child, 
#teenager, adult, or senior citizen.
age=int(input("Age: "))
if age<=12:
    print("Child")
elif age>12 and age<=19:
    print("Teenager")
elif age>19 and age<=30:
    print("Adult")
elif age>30:
    print("Senior")

#3. Develop a program that prompts the user to enter two numbers and prints out the larger of the two.
n1=int(input("Number 1: "))
n2=int(input("Number 2: "))
if n1>n2:
    print(f"{n1} is lrger number.")
elif n1<n2:
    print(f"{n2} is larger number.")
else:
    print("Both are equal")

#4. Write a Python script to determine whether a given year is a leap year or not
user_year=int(input("Year: "))
if user_year>0:
    if (user_year%4==0 and user_year%100!=0) or user_year%400==0:
        print(f"{user_year} is leap year.")
    else:
        print(f"{user_year} is not leap year.")
else:
    print("Give number must be greater than zero.")

#5. Implement a program that takes a user's input of three numbers and prints out the maximum and minimum among them
n1=int(input("Number 1: "))
n2=int(input("Number 2: "))
n3=int(input("Number 3: "))
if n1>n3>n2:
    print(f"{n1} is maximum number")
    print(f"{n2} is minimum number")
elif n1>n2>n3:
    print(f"{n1} is maximum number")
    print(f"{n3} is minimum number")
elif n2>n3>n1:
    print(f"{n2} is maximum number")
    print(f"{n1} is minimum number")
elif n2>n1>n3:
    print(f"{n2} is maximum number")
    print(f"{n3} is minimum number")
elif n3>n2>n1:
    print(f"{n3} is maximum number")
    print(f"{n1} is minimum number")
elif n3>n1>n2:
    print(f"{n3} is maximum number")
    print(f"{n2} is minimum number")
else:
    print("No number should be equal to another.")

#6. Create a program that asks the user to enter their exam score and prints out their grade based 
#on the following criteria: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60). 
score=int(input("Score: "))
if score>=90 and score<=100:
    print(f'Grade: "A"')
elif score>=80 and score<=89:
    print(f'Grade: "B"')
elif score>=70 and score<=79:
    print(f'Grade: "C"')
elif score>=60 and score<=69:
    print(f'Grade: "D"')
elif score<60:
    print(f'Grade: "F"')
































