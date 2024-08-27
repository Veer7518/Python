class Person:
    name="veer singh"

    def changeName(self,name):
        Person.name = name

obj=Person()
obj.changeName("Rahul singh")
print(obj.name)
#print(Person.name)
