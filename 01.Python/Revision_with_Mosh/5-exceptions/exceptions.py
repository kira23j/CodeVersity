# exceptions
try:
    age = int(input("Age:"))
except ValueError as ex:
    print("you din enter valid age.")
    print(ex)
    print(type(ex))
else:
    print("no exceptions were thrown")
print("execution continues")

# handling different exceptions
try: 
    age = int(input("Age: "))
    xfactor = 10 / age
except (ValueError, ZeroDivisionError):
    print("you din enter a valid age")
else:
    print("no exeptions were thrown")
finally:
    print("this block will always run")

def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age must be positive")
    xfactor = 10 / age
    return xfactor

try:
    calculate_xfactor(-1)
except ValueError as ve:
    print(ve)

 