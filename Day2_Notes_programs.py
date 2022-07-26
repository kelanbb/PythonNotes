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

    
# FILE STUFF-----------------------------------------
  1 #!/usr/bin/python3
  2 
  3 with open('withOpenTest.txt', 'w')as myfile:
  4    myfile.write(" my first line of text gabagoo ye") #writes a line, ov    errtes
  5 mylist = ["one big mama\n", "two joe mamas\n", "three yo mamas\n"]
  6 with open('withOpenTest.txt', 'w')as myfile1:
  7    myfile1.write(mylist)
  8 
  9         # writelines writes a list of strings to file
 10 
 11 #next, READ from a file
 12 with open('withOpenTest.txt', 'r')as myfile2:
 13    content = myfile2.readline #or just .read(10)-- reads first 10 bytes     of file (or .readlines?) to not read one line
 14    print(content)
~                           
