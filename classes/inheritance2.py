

#Ecomerce

class User():

    def __init__(self,name,email,phone,password,user,discount=0):
        self.name=name
        self.email=email
        self.phone=phone
        self.password=password
        self.discount=discount
        self.user=user
        self.is_locked=False

    def say_my_name(self):
        print(f"My name {self.name}")
    
    def print_details(self):
        print("-----------------")
        print("User",self.user)
        print("Name",self.name)
        print("Email",self.email)
        print("Phone",self.phone)
        print("Discount",self.discount)
        print("-----------------")

    def login(self):

        if self.is_locked:
            print("Account already locked")
            return

        for i in range(1,3):
            password=input(f"Enter your password: Attempt {i}")  
            if self.password==password:
                print("Logged in success")
                return
        self.is_locked=True
        print("Account locked contact admin")
                      

class Employee(User):
    
    def __init__(self, name, email, phone,password,salary):
        super().__init__(name=name, email=email, phone=phone,password=password,discount=10,user="employee")
        self.salary=salary

class Customer(User):
    
    def __init__(self, name, email, phone,password):
        super().__init__(name=name, email=email, phone=phone,password=password,discount=0,user="customer")
        


emp1=Employee(name="Sam",email="sam@sam.com",phone=1234234,
              password=1234,salary=20000)

c1=Customer(name="Delilah",email="del@gmail.com",phone=2343,password=1234)

emp1.say_my_name()
c1.say_my_name()

emp1.print_details()
c1.print_details()

emp1.login()