# lists are mutable data structures unlike strings
cities_in_ethiopia=["adissababa","bahirdar","debrebirhan","hawassa","jimma","mekele","gonder"]

# check city in key-word boolean
if "hawassa" in cities_in_ethiopia:
    print("yap it is on the list")

# select a city 
print(cities_in_ethiopia[3])
print(cities_in_ethiopia[-3])
# find a single char from it
print(cities_in_ethiopia[3][2])
# slicing a list [start,end)
print(cities_in_ethiopia[1:4])
# reverse a list
print(cities_in_ethiopia[::-1])

# iterating over a list
for city in cities_in_ethiopia:
    print(city)

# reverse and cound char len of each list items
for char in reversed(cities_in_ethiopia):
    print(f"{char} has a length of {len(char)} characters. \n \n")

# the enumerate function.
for index,city in enumerate(cities_in_ethiopia):
    print(f"{city} is found on number {index+1} in the list.")
    
# the range function upto the range
for city in range(3):
    print(cities_in_ethiopia[city])
print("\n")
# slicing with range by steps
for city in range(0,7,3):
    print(cities_in_ethiopia[city])

# assign a list
cities_in_ethiopia[0]="Desse"
print("\n",cities_in_ethiopia[0])

# assign more than one list
cities_in_ethiopia[1:3]=["arbaminch","wolayta"]
print(cities_in_ethiopia[1:3])

# using append method 
cities_in_ethiopia.append("diredawa")
print(cities_in_ethiopia)

# using extend method we can add multiple values.
cities_in_ethiopia.extend(["axum","Lalibela"])
print(cities_in_ethiopia)

# use insert method to add at the given index of a list
cities_in_ethiopia.insert(1,"Adama")
print(cities_in_ethiopia)

# pop for removing an elemnt from end or by index
cities_in_ethiopia.pop()
cities_in_ethiopia.pop(1)
print(cities_in_ethiopia)

# del for removing by index slice
del(cities_in_ethiopia[1:3])
print(cities_in_ethiopia)

# remove method for deleting by value
cities_in_ethiopia.remove("jimma")
print(cities_in_ethiopia)

# sort method for sorting 
cities_in_ethiopia.sort()
# reverse method for reversing
cities_in_ethiopia.reverse()
print(cities_in_ethiopia)

# count method to count for values
print(cities_in_ethiopia.count("hawassa"))

# index method for showing the index of given list
print(cities_in_ethiopia.index("gonder"))

# copy method will give us brand new copy of list
cities_copy=cities_in_ethiopia.copy()
print(cities_copy)

# use split method to make a list from string separated by a given delimiter.
other_cities="debrebirhan, bahirdar, gambella"
print(other_cities)
print(other_cities.split(", "))

# join method will do opposite of split
print(other_cities.join("-"))

# zip function for multiple lists in one.
print(zip(cities_copy,cities_in_ethiopia))


# multidimensional lists
multi_dl=[cities_in_ethiopia,cities_copy]
print(multi_dl)

# list comprehension:- generate a list from other list.
numbers=[1,2,3,4,5,6]
squares=[]
for number in numbers:
    squares.append(number**2)
print(squares)
