user=input("Enter date: ")
with open("to_do list","r") as f:
    data=f.read()
    my_dict=eval(data)
    for key in my_dict.keys():
        for key, value in my_dict[key].items():
            if key==user:
                print(f"{key}:{value}")