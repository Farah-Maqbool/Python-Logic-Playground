#Meeting Scheduler: Design a program that helps users find a common meeting time among a 
#group. Use if-else statements to check for available time slots in each user's calendar and 
#suggest suitable meeting times.

user1={
    "1/1/2024":"Available",
    "2/1/2024":"Unavailable",
    "3/1/2024":"Available",
    "4/1/2024":"Unavailable",
    "5/1/2024":"Unavailable",
    "6/1/2024":"Available"
}
user2={
    "1/1/2024":"Unavailable",
    "2/1/2024":"Unavailable",
    "3/1/2024":"Available",
    "4/1/2024":"Unavailable",
    "5/1/2024":"Available",
    "6/1/2024":"Available"
}
user3={
    "1/1/2024":"Unavailable",
    "2/1/2024":"Available",
    "3/1/2024":"Available",
    "4/1/2024":"Unavailable",
    "5/1/2024":"Available",
    "6/1/2024":"Available"
}
user=input("Date: ")
for key1, values1 in user1.items():
    if user==key1:
        for key2, values2 in user2.items():
            if user==key2:
                for key3, values3 in user3.items():
                    if user==key3:
                        if values1==values2==values3=="Available":
                            print(f"All members are Available on this date {user}")
                        else:
                            print("No all memebrs availble on this date")















