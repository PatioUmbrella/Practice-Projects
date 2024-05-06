#Class Stuff

#***LONG STORY SHORT***

#self lets you use classes methods on instances of classes!

#Init/ constructor is just a function that sets up the class
#Methods can be used from class object when you make a 'base' object into an instance of a class!
#You can make objects move! - classes are objects and classes can have methods in them which make instances of instances objects move

class House:
    def __init__(self, address, city, state):
        self.address = address
        self.city = city
        self.state = state
    def return_address(self):
        print("Address is " + self.address)

#Both selfs above refer to the H1 instance

#H1 and H2 below are instances of a class

H1 = House("100 Oak St.", "Oakland", "CA")

H2 = House("100 Pine St.", "Seattle", "WA")

H1.return_address()
H2.return_address()