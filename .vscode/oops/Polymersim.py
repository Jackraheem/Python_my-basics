class student:
    name="john"
    __age=20
    def display(self):
        print("it's displaying")

obj= student()
print("name =",student.name)
print("age=",student.age) #here error occurse because of private can't be accessed by outside of the class
       