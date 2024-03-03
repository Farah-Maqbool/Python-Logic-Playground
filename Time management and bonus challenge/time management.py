#1. To-Do List: Develop a program that allows the user to add tasks to a to-do list. Use if statements 
#to categorize tasks as urgent, important, or less important based on their due date and priority.

task_t={
    "urgent":{

    },
    "important":{

    },
    "less important":{

    }
}

to_do=task_t.copy()
while True:
    for key in to_do:
        priority=input("Task (Urgent, Important, Less important): ").lower()
        if key==priority:
                task_name=input("Task Name: ")
                task_date=input("Task Date: ")
                task_t[key][task_date]=task_name
                if input("Do you want to continue (y or n): ")=="n":
                    break
    if input("Do you want to continue (y or n): ")=="n":
        break

with open("to_do list","w") as f:
     f.write(str(task_t))
