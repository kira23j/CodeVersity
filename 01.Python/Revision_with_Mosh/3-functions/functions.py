def hello_func():
    print("hello func")

# arguments 

def hello_person(first_name , last_name):
    print(f"{first_name} {last_name}")
    
hello_person("neil", "armstrong")

# keyword argument
def increment(number, by):
    return number + by

print(increment(2, by=1))

# default argument

def decrement(number, by=2):
    return number - by

print(decrement(3))

# xargs

def multiply(*numbers):
    print(numbers)
    
multiply(1, 2, 3, 4, 5)
    
# kwargs

def save_user(**user):
    print(user["name"])
    
save_user(id=1, name="kira", age=22)

# scope

outer_message = "a"
def greet(name):
    global outer_message
    outer_message = "b"

greet("kira")
print(outer_message)
