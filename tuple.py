a=("jack","gllow","john","jam")
print(len(a))
# tuple methods
#indexing tuple methods
a1=("jack","gllow","john","jam")
print(a1[1])
#updating the item into tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
#replace the tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)



#adding tuple
t1=("red_color","orange_color","black_color")
t2=("red","orange","black")
t3=t1+t2
print(t3)

#multiple tuple
fruit =("froo","hjoo","blue")
tuplee= fruit *2
print(tuplee)

#counting tuples
c=(1,3,7,8,5,4,6,8,5)
c1=c.count(5)#tells the duplication count
print(c1)

#indexin' value tuple
cc=(1,4,5,3,5,32,56,6,9)
cc1 = cc.index(32) #its shows the value of index 
print(cc1)

#unpack the tuple items
fruits=("orange","jack fruit","mango")
(yellow,red,*blue) = fruits
print(yellow)
print(blue)




