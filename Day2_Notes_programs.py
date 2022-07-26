#!/use/bin/python3

# counts and while loop
#break command, breaks out of loop or iteration


count = 0

while count < 10:
  count += 1
  print("Count is {}".format(count))
  if count == 5:
    print("Count is 5")
    break                             # break
    
    
# strings and character lists
a = wadawdawdgrgrgrzkgjnagl
list (a) # list function turns string or whatever into a list of characters
range(0,100) #
list(range(0,100)) # creates a list of int from 0 to 99 ( 100 total)

# LIST LOOP PROGRAM--------------------

mylist = list(range(21)) # goes from 0 to 20, 21 not included

newlist = []

for num in mylist:
   print(num * 3)
   newlist.append(num*3)

for x in newlist:
   print(x/3)

mytuple = ("a","b","C","D")

for num in mytuple:
   print("current uple: " +num)
