#1. Design a Python program that calculates the total cost of items purchased by a customer based 
#on the provided unit price and quantity, applying a discount of 10% if the total cost exceeds 
#$1000.
sum=0
while True:
    item=input("Item Name: ")
    price=int(input("Price: ").replace("$",""))
    quantity=int(input("Quantity: "))
    sum+=(price*quantity)

    if input("Do you want to continue (y or n): ")=="n":
        break
if sum<1000:
    total_cost=str(sum-(sum*0.1))
    print(f"Total Cost is ${total_cost}")
else:
    print(f"Total cost is ${sum}")

#2.Develop a program that prompts the user to enter their current temperature in Celsius and 
#prints out whether they should wear a jacket (if temperature is below 20°C) or not.
temperature=int(input("Temperature: "))
if temperature<20:
    print("Wear Jacket")
else:
    print("No need to wear jacket")

#3. Write a Python script that takes a user's input of three sides of a triangle and determines 
#whether it is equilateral(a=b=c), isosceles(a=b,a=c,b=c), or scalene.(a!=b!=c)
print("Tringle sides")
sides_1=input("Side 1: ")
sides_2=input("Side 2: ")
sides_3=input("Side 3: ")
if sides_1==sides_2==sides_3:
    print("Equilateral Triangle")
elif sides_1==sides_2 or sides_1==sides_3 or sides_2==sides_3:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

#4. . Create a program that simulates a simple ATM machine. It should ask the user for their PIN, 
#verify it, and then allow them to withdraw money if the balance is sufficient
atm_code={"3492":50000,"2356":30000,"4376":10000}
pin=input("PIN: ")
for key , values in atm_code.items():
    if key==pin:
        amount=int(input("Amount: "))
        if amount<=values:
            print("Take money")
            break
        else:
            print("Your balance is Insufficient")
            break

#5. Develop a Python script that takes a user's input of a month (as a number) and prints out the 
#number of days in that month.
month_day={"1":31,"2":29,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
month=input("Month: ")
for key, values in month_day.items():
    if key==month:
        print(f"{values} days in that month")

#6. Implement a program that takes a user's input of a year and month and prints out the number 
#of days in that month, considering leap years
month_day={"1":31,"2":28,"3":31,"4":30,"5":31,"6":30,"7":31,"8":31,"9":30,"10":31,"11":30,"12":31}
year=int(input("Year: "))
month=input("Month: ")
if (year%4==0 and year%100!=0) or year%400==0:
    month_day["2"]=29
for key, values in month_day.items():
    if key==month:
        print(f"The Year {year} have {values} days in {month} month")






