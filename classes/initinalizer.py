
#initializer:constructor

#Speical method in a class
#initializer: method is called whenever the blueprint is used
#To create an object
#method function is inside a class

#method your create you have to have the self: key worked
class Human():

    def __init__(self,gender,name):
        print("The initializer wass called")
        self.gender=gender
        self.name=name
        if self.gender=="Male":
            self.ribs=24
            self.curse="Suffer"
        else :
          self.ribs=23
          self.curse="Pain"
        

    def print_self(self):
        print("----------------------")
        print("name",self.name)
        print("gender",self.gender)
        print("ribs",self.ribs)
        print("curse",self.curse)
        print("---------------------")
    
# adam=Human(name="adam",gender="Male") #object from a class
adam=Human(name="adam",gender="Male")
adam.print_self()

eve=Human(name="eve",gender="Female")
eve.print_self()
# eve=Human(name="eve",gender="Female")
# print("name",eve.name)
# print("gender",eve.gender)
# print("ribs",eve.ribs)
# print("curse",eve.curse))