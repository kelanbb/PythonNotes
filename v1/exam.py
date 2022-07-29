
#!/usr/bin/env python3

def q1(floatstr):
    ''' 
    TLO: 112-SCRPY002, LSA 3,4
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the 
    argument as elements in the list.
    '''
    spl= floatstr.split(",")
  #  [float(i) for i in spl] ...... will turn each element into a float in spl
    return [float(i) for i in spl] # list comprehension..?

   #return list(map(float, floatstr.split(',')))  #every element in this list will be a float, gets saved as map obj. then typecast to list
   # map func takes function on left and puts it on interval to the right

def q2(*args):
    ''' 
    TLO: 112-SCRPY006, LSA 3
    TLO: 112-SCRPY007, LSA 4
    Given the variable length argument list, return the average
    of all the arguments as a float
    '''
    return(sum(args)/len(args))


def q3(lst,n):
    ''' 
    TLO: 112-SCRPY004, LSA 3
    Given a list (lst) and a number of items (n), return a new 
    list containing the last n entries in lst.
    '''
    x = []
    for i in range(len(lst)-n,len(lst)):
      x.append(lst[i])
    return x
    
    #return lst[-n:] #only having one colon will go to end

    
def q4(strng):
    ''' 
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY006, LSA 3
    Given an input string, return a list containing the ordinal numbers of 
    each character in the string in the order found in the input string.
    '''

    x = []
    for i in strng:
       x.append(ord(i))
    return x
   
    ''' 
    #method 2
    return [ord(i) for i in strng] # list comprehension, again
    method 3
    return list(map(ord,string)) #ords every character in that string
    # map takes 2 args, arg1 is function, 2nd arg is interable object, does function to the object
    '''

def q5(strng):
    '''
    TLO: 112-SCRPY002, LSA 1,3
    TLO: 112-SCRPY004, LSA 2
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    y = strng.split(" ")
    return tuple(y)

def q6(catalog, order):
    '''
    TLO: 112-SCRPY007, LSA 2
    Given a dictionary (catalog) whose keys are product names and values are product
    prices per unit and a list of tuples (order) of product names and quantities,
    compute and return the total value of the order.

    Example catalog:
    {
        'AMD Ryzen 5 5600X': 289.99,
        'Intel Core i9-9900K': 363.50,
        'AMD Ryzen 9 5900X': 569.99
    }

    Example order:
    [
        ('AMD Ryzen 5 5600X', 5), 
        ('Intel Core i9-9900K', 3)
    ]

    Example result:
    2540.45 

    How the above result was computed:
    (289.99 * 5) + (363.50 * 3)
    '''
    total = 0
    for j in order:
      if j[0] in catalog.keys():
         total +=  float(catalog[j[0]] * j[1])
    return total

    '''
    total = 0
    for product, quanity in order: # will make product equal to the fitsr index in the tuple, quanity, 2nd index, but overall still loops through each element, just breaks town te tuple element in the loop
    
      total += catalog[product] * quanity
    return total

    #method 3

    return sum(catalog[pruduct]*quanity for product,quanity in order
    #condenses method 2
    '''

def q7(filename):
    '''
    TLO: 112-SCRPY005, LSA 1
    Given a filename, open the file and return the length of the first line 
    in the file excluding the line terminator.
    '''
    with open (filename, 'r') as f:
       #return len(fp.readlines()[0]) -1 )
       content =(f.read()).split('\n')
    return len(content[0])



def q8(filename,lst):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1,2
    TLO: 112-SCRPY005, LSA 1
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in 
    the list. If "stop" is not found in the list, write the entire list to 
    the file on separate lines.
    '''
    with open (filename, 'w')as f:
       for x in lst:
          if 'stop' in x:
             break
          else:
            f.write(x + "\n")

    '''
    with open(filename, 'w') as fp:
      for i in lst:
         if i.lower() == 'stop':
            break
         fp.write(f'{i}\n') #f is .format shorthand, i is that you want to write, same as ({}\n).format(i)
    '''

def q9(miltime):
    '''
    TLO: 112-SCRPY003, LSA 1
    Given the military time in the argument miltime, return a string 
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    if 300<=miltime<=1159:
       return "Good Morning"
    elif 1200<=miltime<=1559:
       return "Good Afternoon"
    elif 1600<=miltime<=2059:
       return "Good Evening"
    elif 2100<=miltime<=2359 or miltime <= 259:
       return "Good Night"
    else:
       return miltime

def q10(numlist):
    '''
    TLO: 112-SCRPY003, LSA 1
    TLO: 112-SCRPY004, LSA 1
    Given the argument numlist as a list of numbers, return True if all 
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    for x in numlist:
       if x < 0:
         return False
    return True

    #return all(map(lambda x : x >= 0,numlist))  #lambda makes a simple function, all checks interval ,if al true then true if any false fasle

                                                                                                  

