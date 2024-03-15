def hello_there(fn):
    def inner(*args,**kwargs):
        print("hello there")
        fn(*args,**kwargs)
        print("hello pyhon guy")
    return inner
@hello_there
def welcome(stakeholder):
    print(f"hello {stakeholder} welcome!!")
welcome("kirubel")
def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you! I'm honored to execute your function for you!")
        print(args)
        print(kwargs)
        fn(*args, **kwargs)
        print("It was my pleasure executing your function! Have a nice day!")

    return inner

@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Something complex for our {position} {stakeholder}!")