print("hello jack")
#default parameters
def defaul(country="india"):
    print("this is "+country)

defaul("USA")
defaul("UK")
defaul("Norway")

#Arbitary keyword arguments

def my_function5(**kid):
  print("His last name is " + kid["lname"])

my_function5(fname = "Tobias", lname = "Refsnes") 
