#public

"""class Person:
    name ="anonymous"
    def hello(self):
        print("Hello Person!")

    def welcome(self): 
      self.hello
p1 = Person()   
print(p1.hello())"""

#private

class Person:
    name ="anonymous"
    def __hello(self):
        print("Hello Person!")

    def welcome(self): 
      self.hello
p1 = Person()   
#print(p1.hello())
print(p1.welcome())

