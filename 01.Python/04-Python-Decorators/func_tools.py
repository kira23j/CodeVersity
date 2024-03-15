import functools

def be_nice(fn):
  @functools.wraps(fn)
  def inner(*args, **kwargs):
    print("Nice to meet you! I'm honored to run your function for you!")
    result = fn(*args, **kwargs)
    print("It was my pleasure executing your function! Have a nice day!")
    return result
    
    return inner


@be_nice
def complex_business_sum(a, b):
  "Adds two numbers together"
  return a + b

help(complex_business_sum)