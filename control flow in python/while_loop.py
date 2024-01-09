#while loop can used to execute the statement gets true
i = 1
while i < 6:
  print(i)
  i += 1

#break the loop

i=1
while i<6:
  print(i)
  if(i==3):
    break
  i +=1  

#continoue
i=1
while i<6:
  i +=1
  if(i==3):
    continue
  print(i)

#else using the loop while
i=1
while i<6:
  print(i)
  i+=1 
else:
  print("i is not no longer 6")    
