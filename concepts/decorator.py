#Decorators
# Extend or modify the behaviour of 
## functions or without changing their code 
## CALLBACK<->HOF


def my_deco(func):
    def wrapper():
      print("Before function run")
      func()
      print("Function completed running")
    return wrapper

# @my_deco
def hello():
    print("Hello world")

my_deco(func=hello)()

# hello()