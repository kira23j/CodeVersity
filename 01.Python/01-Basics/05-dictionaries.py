# unordered data structure for relationships with key and values,keys must be immutable
fname=input("please enter ur first name: ")
lname=input("please enter ur last name: ")
age=input("please enter ur age: ")
job=input("please enter ur job: ")


ethiopian_form={
    "fname":fname,
    "lname":lname,
    "age": age,
    "job":job,
    "fav-thing":["movie","sport","anime"]
    
}
print(ethiopian_form)
# adding a new key value pair
ethiopian_form["nationality"]="ethiopian"
print(ethiopian_form)

# modifying the existing key value pair.
ethiopian_form["fav-thing"]=["music","anime","sport"]

# how many times each word in list is mentioned.
fav_thing=["sports","anime","movie","anime","sports","sports"]

def count_words(fav_thing):
    counts={}
    for word in fav_thing:
        if word in counts:
            counts[word]+=1
        else:
            counts[word]=1
    return counts
print(count_words(fav_thing))

# get values using keys with get and setdefault
num={
    1:3,
    2:5,
    3:7
}
print(num.get(3))
print(num.setdefault(3))

# pop from dic using key
num.pop(1)
print(num)

# clear method to remove all the key value pairs.
num.clear()
print(num)

# update method for updating dic using another dic
num2={
    1:2,
    3:4,
}
num.update(num2)
print(num)

# dict key word for changing to dictionary.
num3=[[1,2],[5,6],[3,4]]
print(dict(num3))

# nested dictionaries
my_hero_academia={
    "season_one":{
        "episodes":13,
        "genre":"introduction"
    },
    "season_two":{
        "episodes":24,
        "genre":"motivation"
    }
}
print(my_hero_academia["season_two"]["episodes"])

# dictionaries iteration.
anime_rating={
    "death-note":9.2,
    "my-hero-academia":8.5,
    "classroom-of-the-elite":7.6,
    "your-lie-in-april":8.2
}
for anime in anime_rating:
    print(f"the name of anime is {anime} which has rating of {anime_rating[anime]}")

# iterate using items() method
for key,value in anime_rating.items():
    print(f"The name of anime is {key} which has rating of {value}")
    
# using keys and values methods.
print("list of anime",anime_rating.keys())
print("rating for the list of anime",anime_rating.values())

# sorted function for ordering
print(sorted(anime_rating))

# list of dictionaries.
animes=[
    {"name":"deathnote","rating":9.2},
    {"name":"my-hero-academia","rating":8.5},
    {"name":"classroom-of-the-elite","rating":8.7}
]
for anime in animes:
    for key,value in anime.items():
        print(f"{key} is {value}")

# using keyword argument we can convert to dic
def let_num(**kwargs):
    print(kwargs)
    total=0
    for num in kwargs.values():
        total+=num
    print(f"the sum of values is {total}")

let_num(a=1,b=2,c=3,d=4,e=5)

# args and kwargs for tuple and dictionary generation.
def arg_kwarg(a,b,*args,**kwargs):
    print(f"the first two values are {a, b}")
    print(f"the sum of the 2 values is {a+b}")
    print(f"the  other values are {args}")
    argt=0
    for arg in args:
        argt+=arg
    print(f"the sum of other values is {argt}")
    total=0
    for sum in kwargs.values():
        total+=sum
    print(f"the newly assigned values are {kwargs}")
    print(f"the sum of newly assined values is={total}")
    
arg_kwarg(1,2,3,4,5,e=4,f=5,g=6)
    
# unpacking argument dictionary meter and cm to mm
def mtomm(meters,centemeters):
    mtomilli=1000*meters
    cmtomilli=10*centemeters
    return mtomilli + cmtomilli

stats={
    "meters":10,
    "centemeters":3
}
print(f"when {stats['meters']} meters and {stats['centemeters'] } centimeters converted to millimeters the value is : ",mtomm(**stats), "millimeters.")

# dictionary comprhension from list and string


all_english="the quick brown fox jumps over the lazy dog."

letter_counts={letter:all_english.count(letter) for letter in all_english}

print(letter_counts)

programming_language=["python","javascript","dart","typescript"]

length={language:len(programming_language) for language in programming_language if "p" in language}

print(length)

# dictionary from dictionary inverting capital and state from state and capital.
ethio_state_capital={
    "amhara":"bahirdar",
    "oromiya":"jimma",
    "tigray":"mekelle",
    "afar":"semera"
}

inverted={capital:state for state ,capital in ethio_state_capital.items()}
print(inverted)