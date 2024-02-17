# for loops in python
# iterable obj=list,dict,tuple,set and string
iterable_object=[1,2,3,4,5]
for item in iterable_object:
    print(item)
for number in range(9):
    print(f"hello there {number} times")

# while loops
num=0
while num<10:
    print(f"{num} times hello there")
    num+=3
while True:
    x=input("enter -1 to exit  0 to infite loop and 1 to continue: ")
    x=int(x)
    if x==-1:
     break
    elif x==0:
        print("loop")
    elif x==1:
        continue

    
    