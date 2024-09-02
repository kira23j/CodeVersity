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

