dist={
    "name":"jack",
    "age":22,
    "Id":"f321hyi7"
}
print(dist)
print(len(dist))
print(dist["age"])

#changing the values by using dictionary

dist1={
    "name":"john",
    "age":25,
    "Id":"f321hyi76",
    "year":1980
}
dist1["year"]= 2018
print(dist1)

#updating the value

thisdist={
    "name":"jack",
    "age":22,
    "Id":"f321hyi7"
}
thisdist.update({"salary":50000})
print(thisdist)

#remove the key 
r={
    "name":"jam",
    "age":20,
    "Id":"f32i7"
}
r.pop("age")
print(r)

#looping
l={"name":"joo",
    "age":22,
    "Id":"f327hyi7"
 }

for i in l.values():#it's only shows the values not keys
    print(i)

#nested dictionary

employees={
    "e1":{
          "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
    },
    "e2":{
          "name":"jam",
    "age":21,
    "id":2347,
    "salary":"7lpa"
    },
    "e3":{
          "name":"Abella",
    "age":26,
    "id":2344,
    "salary":"15lpa"
    }
}
print(employees)
print(employees["e3"])#accesss the one object

#items
i={
    "name":"Buggati",
    "model":"chiron",
    "year":2015
}
x=i.items()
print(x)

#default key setting
d={
      "name":"Buggati",
      "model":"Divo",
      "year":2017
}
y=d.setdefault("model","Divo")
print(y)

#popitem used to remove the last item
ii={
      "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
ii.popitem()
print(ii)

2
ii={
      "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
z=ii.popitem()
print(z)#here only shows the last item of salary key
#del method in dictonary
de={
    "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
del de["salary"]
print(de)

#clear method in dictonary
c1={
    "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
c1.clear()
print(c1)

#looping in dictionary
l1={
    "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
for x in l1:
    print(x)

#looping in the dictionary only print values
lv={
    "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}

for y in lv.values():
    print(y)

#looping in the dictionary only print keys
ke={
    "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
for z in ke.keys():
    print(z)

#loop print the items in the dictionary
it={
    "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
for a,b in it.items():
    print(a,"=",b)

#copy the dicionary
co={
    "name":"jack",
    "age":22,
    "id":2345,
    "salary":"5lpa"
}
myco=co.copy()
print(myco)   






