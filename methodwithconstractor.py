class Student:
    collage_name="ABC Collage"

    def __init__(self,name,marks,parsent):
     self.name = name
     self.marks= marks
     self.parsent = parsent

    def welcome(self):
     print("Welcome student",self.name)

    def welcome1(self):
     print("parsent",self.parsent)

    def get_marks(self):
      return self.marks
    
    
obj= Student("veer",99,98)
obj.welcome()
obj.welcome1()
print("mark",)
print(obj.get_marks())
