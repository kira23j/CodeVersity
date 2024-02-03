all_english="The Quick Brown Fox Jumps Over The Lazy Dog"
stars="***"

# length of string
print(len(all_english),len(stars))
# multiply strings 
print(stars*50)
# indexing strings
print(all_english[0],all_english[4**2],all_english[-2])
#string slicing
print(all_english[0:3])
print(all_english[3:])
print(all_english[:10])
print(all_english[:-3])
# copy string
print(all_english[:])
# slicing by steps ,[start,end,step]
print(all_english[0:10:3])
print(all_english[-7:-2:2])
# reverse a string
print(all_english[::-1])
print(all_english[::-3])
# escape char for string 
print("\t Hello there \n \"welcome to python\" ")
# in operator boolean
print("quick" in all_english,"Quick" in all_english)

# string methods
# ===========
# find method it'll return -1 if not found
print(all_english.find("e"))
print(all_english.find("e",10))
print(all_english.find("2"))

# index method it crash if not found
print(all_english.index("z"))

# startswith and endswith boolean
print(all_english.startswith("The"))
print(all_english.endswith("Fox"))

# count method
print(all_english.count("e"))

# capitalize=first letter, title=all first letters , lower=all small , upper=all upper and swapcase=interchange
print(all_english.capitalize())
print(all_english.title())
print(all_english.upper())
print(all_english.lower())
print(all_english.swapcase())

# method chaining
rand=all_english.capitalize().swapcase().title()
print(rand)
# lstrip=remove left space,rstrip=remove right space,strip=remove both
center="   hello   python   "
print(center)
print(center.lstrip())
print(center.rstrip())
print(center.strip())

# Replace 
phone_num="555 555 555 1234"
print(phone_num.replace(" ","-"))

# format method 
missing="{} quick {} fox {} over {} lazy {} "
print(missing.format("the","brown","jumps","the","dog"))

sentence="I'm {name}, and I'm From {city}"
name=input("enter ur name: ")
city=input("enter your city: ")
print("with format method: ",sentence.format(name=name,city=city))


# using formated string (f string)

print("with f string: ",f"I am {name} and I am from {city}")
