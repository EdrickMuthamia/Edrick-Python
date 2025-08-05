

## greets: funciton <name> (<parametrs>){}
def greet(name,country):

    def inner():
        print("This is the inner function")

    outer()
    inner()
    print(name,country)
    print("Hi ",name," Your favourite country",country)
    print(f"Hi {name} Your favourite country {country}")


def outer():
        print("This is the outer function")

greet("Sam","Germany")
greet("JOHN","Kenya")