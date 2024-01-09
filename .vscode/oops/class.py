#class can have attribute and methods
#class have data and functions

class student:
    #instance variables
    roll_number=123
    name="jack"
    branch="cse"
#function represtation
    def read(self):
        print("reading")
#object represtation 
abs=student()
print("roll",abs.roll_number)
print("name",abs.name)
print("branch",abs.branch)
abs.read() 

print("\n")

#example 2

class student:
    #instance variables
    roll_number=123
    name="jack"
    branch="cse"
#function represtation
    def read(self):
        #giving an local variable 
        id=35643692
        print("id=",id)
        print("roll_number",self.roll_number)
        print("reading")
    def writting(self):
        print("writting")    
#object represtation 
abs=student()
hh=student()
print("roll",abs.roll_number)
print("name",abs.name)
print("branch",abs.branch)
abs.read() 
hh.writting()   
