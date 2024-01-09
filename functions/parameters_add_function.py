def myfunction(first_name):
    print(first_name + "jack sparrow")

myfunction("email of"+"\t") 

# passing two parameters
def myfun(email,password):
    print(email+"\n"+password)

myfun("jackse@gmail.com","hdvfgye6742") 


#Arbitary arguments *key
def multi(*names):
    print("my name is"+names[3]) #here one argument only taking

multi("jack","john","jam","Abella","Danger")  

#Arbitary keyword argument **key

def my_function5(**kid):
  print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes") 

#default parameters
def defaul(country="india"):
    print("this is "+country)

defaul("USA")
defaul("UK")
defaul("Norway")    


#key word arguments

def keyyy(p1,p2,p3):
    print("here p2 is greater"+"\v"+p2)

keyyy(p1="jack",p2="dani danials",p3="john") 


