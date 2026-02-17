def check_the_magic(**kwargs):
    print(f"The data type is:", {type(kwargs)})
    print(f"The data is:", {kwargs})
    print(f"The keys are:", {kwargs[location]})


def check_the_magic2(name, age, location):
    print(f"name is {name}")
    print(f"age is {age}")
    print(f"location is {location}")

check_the_magic("Joseph", 34, "kenya")
