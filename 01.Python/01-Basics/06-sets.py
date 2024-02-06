# mutable ,unordered ds with immutable elements

first_sets={1,2,3,(1,2,3)}
print(first_sets)
# duplicated values are considered as one.
remove_duplicate={(1,2,3),(1,2,3),(1,2,3)}
print(remove_duplicate)

# square a num
squares={number**2 for number in [-5,-4,-3,-2,-1]}
print(squares)

# set function
print(set("abcded"),set("12345"))

# add method for single and update for multiple values.
set={"a","b","c"}
set.add("d")
set.update("e","f","g")
print(set)

# remove deletes with exception ,discard deletes with no exception
set.remove("a")
set.discard("b")
#  set.remove("z")-this will throw an error but not discard.
set.discard("z")

# intersection method for intersection of 2 sets
items_one={"pens","pencils","papers","phone"}
items_two={"charger","phone","laptop"}
items_intersection=items_one.intersection(items_two)
print(items_intersection)

# union method for union
items_union=items_one.union(items_two)
print(items_union)

# difference method unique value of first set
items_x_y=items_one.difference(items_two)
print(items_x_y)

# symmetric difference for values not shared by both sets.
items_semetric_d=items_one.symmetric_difference(items_two)
print(items_semetric_d)

# issubset and issuperset for checking sub and super set.
print(items_two.issubset(items_one))
print(items_one.issuperset(items_two))
print(items_intersection.issubset(items_one))