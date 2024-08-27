for number in range(3):
    print("hello", number)
 
for number in range(1,10,3):
    print("hello", number)
    
sample=True
for number in range(3):
    print("attempt")
    if sample:
        print("successful")
else:
    print("attempted")
# nest loop
for x in range(5):
    for y in range(3):
        print(f"(({x},{y}))")  

# iterables 
for x in "hello":
    print(x)
for x in range(5):
    print(x)
for x in [1, 2, 3]:
    print(x)


