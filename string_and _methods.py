s1 ='hello'
print(s1)
s2="hello jack"
print(s2)
s3='''how are you mr.jack!'''
print(s3)

#string methods

a = "jack"
print(a.upper()) #converted into uppercase

b="JACK"
print(b.lower()) #converted into lower

c="john"
print(c.capitalize()) #converted into first letter as capital

d ='john'
d1 = 'jack'
print(d+d1) # concatination

#slice method
e = "hello,world"
print(e[2:5])

e1 = "hello jack"
print(e1[-3:])

e2 = "hello jack"
print(e2[4:6])

#strip
m = "hjjef iwj"
print(m.strip())

#split
n = "hello,jack"
print(n.split(","))

#  string length without using len()
def string_length(string):
    count = 0
    for char in string:
        count += 1
    return count

# Example usage:
my_string="jkdjfhsugh"
length = string_length(my_string)
print("Length of the string:", length)

    

