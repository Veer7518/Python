class Car:
    @staticmethod
    def start():
        print("car is satrt")
        @staticmethod
        def stop():
            print("car stop")
           
class toyotaCar(Car):
        def __init__(self,brand):
         self.brand = brand 

class Fortuner(toyotaCar):
        def __init__(self, types):
           self.types=types

obj = Fortuner("")
obj.start()
                            
