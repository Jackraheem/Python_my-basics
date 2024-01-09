#import the ABC module
from abc import ABC,abstractmethod
class AbstractDemo(ABC):
    #this decorator used for abstract method
    @abstractmethod
    def display(self):
        None
    @abstractmethod    
    def show(self):
        None    

class Demo(AbstractDemo):
    def display(self):
        print("Abstract Method")

    def show(self):
        print("show method")    

class Demo1(AbstractDemo):  #concert class
    def display(self):
        print("Abstract Method")

    def show(self):
        print("show method")    




obj =Demo1()
obj.display()
obj.show()
