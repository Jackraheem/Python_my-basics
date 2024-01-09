#set 
s={1,2,1,2,34,67}
print(s) #set method are basically used to "remove the duplication values"



set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3) #here sets are the shows the end item

s1 = {"abc", 34, True, 40, "male"}

print(s1)

#unorder set
sss=set(("apple","bannana","cherry"))
print(sss)

#add the item
r={"hoodie","t-shirt","shirt"}
r.add("gens")
print(r)

#updating the items
u={"apple","jack_fruit","pomogrant","pinapple",}
u1={"red-wine","black_juice","white-wine"}
u.update(u1)
print(u)

#remove the item from the set
thisset={"jack","john","jax","jim","app"}
thisset.remove("jack") #use the methods of clear() pop() discard()
print(thisset)

#union method in set()
a1={1,2,3,4,45,5}
a2={"red","orange","blue"}
a3=a1.union(a2)
print(a3)

#intersection method() is used to find the duplication
f={"apple","fruit","club"}
f2={"club","cum","claim"}
fn=f.intersection(f2)
print(fn)

fo={"apple","fruit","hooo"}
fo1={"apple","hooo","froo"}
fo.intersection_update(fo1)
print(fo)




