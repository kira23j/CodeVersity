# function in python use def keyword
def output():
    print("hello world")
output()

# parameters and arguments
def sum2(param1,param2):
    print(f"the sum of {param1} and {param2} is {param2+param1}")
arg1=3
arg2=5
sum2(arg1,arg2)

# positional arguments
def add(a,b,c):
    print(f"the sum of {a,b,c} is {a+b+c}")
add(c=3,a=4,b=5)

# return values
def add(a,b,c):
    return a+b+c
print(add(1,2,3))

# default args
def add_default(a=1,b=2):
    return a+b
print(add_default(1))

# function annotation
def word_multiplier(word:str,times:int)->str:
    return word*times
accept=word_multiplier("kira23j",23)
print(accept)
