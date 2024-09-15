# stacks:LIFO last in first out use append and pop in list
#
# queue : FIFO first in first out
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
    
# tuple
point = (1, 2, 3)
print(type(point))
# swap
x = 10
y = 11
x, y = y, x
print(x, y)


# array for performance
from array import array

numbers = array("i", [1, 2, 3])
# numbers[0] = 1.0

# set 

numbers = [1, 2, 3, 4, ]
first = set(numbers)
second = {1, 4}
second.add(5)
second.remove(1)

union = first | second
intersection = first & second
difference = first - second
symmetric_difference = (first ^ second)

print(union, intersection, difference, symmetric_difference)

# dictionaries

point_one = {"x": 1, "y": 2 }
point_two = dict(x=1, y=2)
point_one["x"] = 3
print(point_one, point_two)
if x in point:
    print(point_two["x"])
print(point_two.get("x", 0))
del point_one["x"]
for key, value in point_two.items():
    print(key, value)
    
# dic comprehension
values = {}
values = {x: x * 2 for x in range(5)}
print(values)

# unpacking operator
first = {"a": 1, "b": 2, "c": 3}
second= {"d": 1, "e": 2, "f": 3}
combined = {**first, **second, "z": 1}
print(combined)

# zip                                
print(list(zip("abc", [1, 2, 3])))  
                                                        
