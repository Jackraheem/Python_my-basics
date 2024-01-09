#list "mutable"
l =["herry","jack","taill","global"]
print(type(l),l,id(l))

#list methods
j1=["ford","buggatti","tata","ferry","go","BMW","benz","audi","kuzi","kia","rollsroye","rangerover","mg","jazar"]
print(j1[12])
print(j1[-0])

#changing the item values
iteam = ["danger","nickie brookie","kiara mia"]
iteam[0] = "Abella" #here item will replaced
print(iteam)

#adding item into list

y=["yellow","orange","red","blue"]
y.append("black")
print(y)

z=["yellow","orange","red","blue"]
z.insert(0,"black")
print(z)

#remove the item into list
r=["buggati","chiron","mg"]
r.remove("chiron")
print(r)

#looping the list
fruits= ["bannana","mango","cherry","jam"]
newfr=[]
for x in fruits:
    if 'a' in x:
        newfr.append(x)

print(newfr)

#2

cars =["tata","buggati","chiron","rollsroy","mg"]
newcars =[]
for y in cars:
    if 'b' in y:
        newcars.append(y)

print(newcars)

#sort lists items

s=["red","blue","yellow","white"]
s.sort()
print(s)

s1=["red","blue","yellow","white"]
s1.sort(reverse= True)
print(s1)

#copy list item
c=["red","blue","yellow","white"]
cp = c.copy()
print(cp)


#clear method can be used to remove all items into the list
cc=["red","blue","yellow","white"]
cc.clear()
print(cc)

#pop method
pp=["red","blue","yellow","white"]
x=pp.pop(0)
print(x)

