# function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# in python we define a function using the def keyword followed by the function name and parentheses which may include parameters. The code block within every function starts with a colon (:) and is indented
def greet(): # this is a function definition. greet is the name of the function and name is a parameter that the function takes
    print("Hello! " ) # this is the code block that belongs to the greet function.
    print("Welcome to Python programming!") # this is another line of code that belongs to the greet function.
greet() # this is a function call. 

def area_of_circle(r):
    area = 3.142 * r * r
    print(f"The area of the circle with radius {r} is {area}")
    return area
area_of_circle(5)
area_of_circle(10)