def user_info(name, **kwargs):
   # print(f"Name is : {name}")
   #  print(f"kwargs is : {kwargs}")

   data = ""
    for key in kwargs:
        value = kwargs[key]
        data += f"{key} : {kwargs[key]}\n"
    with open(f"{name}.txt", "w") as file:        
        file.write(data)
        
def collect_user_info():
    name = input("Enter your name: ")
    print ("____________________")
    print("you can fill your bio data here")
    print("enter categories and values")
    print("enter 'done' when you are done")
    print("____________________")
    user_info={}
    while True:
        category_name = input("Enter category: ")
        if category_name == 'done':
            break
        category_description = input("Enter category description: ")
        user_info[category_name] = category_description
        #print(user_info)

    user_info(name, **user_data)

collect_user_info()