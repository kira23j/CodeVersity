letters = ["a", 'b', 'c']
matrix = [[0, 1], [2, 3]]
zeros = [0] * 5
combined = zeros + letters
numbers = list(range(20))
chars = list("welcome")
print(chars)

# Accessing Items

letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
letters[0]
print(letters[0:3])
print(letters[::2])
print(letters[::-1])


# unpacking list
numbers = [1, 2, 3, 5, 7]
first, second, third, fourth, fifth = numbers
print(first, second, third, fourth, fifth)

# packing a list with *
first, second, *other = numbers
print(other)
first, *second, last = numbers
print(second)

# looping over lists
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters):
    print(index, letter)

# adding and removing items from list

# add
letters.append('d')
letters.insert(0, "_")

# remove
letters.pop()
letters.remove('b')
del letters[0:3] 
letters.clear()
print(letters)

# finding items in a list
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
if 'c' in letters:
    print(letters.index('c'))
    
# sorting   
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
numbers.sort(reverse=True)
sorted = sorted(numbers)
print(numbers, sorted)

items = [
    ("product1", 10),
    ("product2", 9),
    ("product3", 12),
    ("product4", 7),
]

# lambda functions

items.sort(key=lambda item:item[1])
print(items)

# map functions

prices = map(lambda item: item[1], items)

# filter functions

filtered = list(filter(lambda item: item[1] >= 10, items))

# list comprehension

prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]

# zip function

list_one = [1, 2, 3]
list_two = [10, 20, 30]
print(list(zip("abc", list_one, list_two)))
