
## *kwargs -> Key word arguments
## Dictionary{key:value}

# 3 min :try mixing up
def greet(name,nationality):
    print("Name is",name)
    print("From ",nationality)



# greet(name="",nationality="")
# greet("Mwange","Kenya")
## greet option to use or not
## let x=20 : Language feature

#KWARGS PROFILE
def employee(**kwargs):
    print(kwargs)
  
    for key,value in kwargs.items():
        print("For key",key, "The value is",value)

#{key:value}
# employee(name="Samson",age=20,degree='Engineering')
# employee(name="Samson",country="Kenya",degree="Engineering")
# # employee("samson","Bio Chemist")


def do_drink(**kwargs):
    drinks=kwargs["drink"]
    prices=kwargs["prices"]

    print(kwargs)

    for index,value in enumerate(drinks):
        print("For index",index)
        print("The Drink",value)
        print("The price",prices[index])


##ARGS AND KWARGS --> DECORATORS
# do_drink(drink=["Glenfidish","KingFisher"],
#          prices=[120,100,40])


def mixed(*args,**kwargs):
    print("Kwargs",kwargs)
    print("Args",args)

mixed("cool","drinks",name="John",age=20)

#Kwargs and args


def square_all(*args):
    ans=[]
    for n in args:
        ans.append(n*n)
    print(ans)
    return ans

square_all(2,4,6,1)