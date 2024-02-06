# if elif and else
prime_numbers=[2,3,5,7,11]
if 3 in prime_numbers:
    if 3==6/2:
        print("yap it is 3")
elif 2 in prime_numbers:
    if 6/3==2:
        print("yap it is 2")
else:
    print("nope it isnot on the list")

# bool function
print(bool(1),bool(-1),bool(0),bool("hello"),bool(""))

age=input("enter your age: ")
age=int(age)
can_enter= "you are allowed" if age>18 else "not allowed"
print(can_enter)

# and or and not key words
if 1==1 and 2==2:
    print("fact")
if 1==1 or 2==1:
    print("hypothesis")
if not 1==2:
    print("rejection")
else:
    print("none")

# nested if statement.
if 1==1:
    if 2==1:
        print("cool")
    else:
        print("bluh bluh bluh")
else:
    print("no way")