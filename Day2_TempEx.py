#!/usr/bin/python3

def main():
   again = 1 
   while again == 1:
      try:
         userInput = input("Enter a temperature (0 to exit): ").upper()
         if (userInput) == "0":
            print("Goodbye")
            again = 0 
         elif  "C" in userInput:
            userTemp = float(userInput.replace("C",""))
            CtoF = ((userTemp * (9/5)) + 32) 
            print ("{}°C = {}°F".format(userInput,CtoF))
         elif "F" in userInput:
            userTemp = float(userInput.replace("F",""))
            FtoC = ((userTemp - 32) * (5/9))
            print ("{}° = {}°C".format(userInput,FtoC))
         else:
            tempSelect = 1 
            while tempSelect == 1:
               whatTemp = input("If this °F or °C?: ").upper()
               if "C" in whatTemp:
                  c2f(userInput)
                  tempSelect = 0 
               elif "F" in whatTemp:
                  f2c(userInput)
                  tempSelect = 0 
               else:
                  print ("Improper format. Enter [C] or [F]")
      except:
         print("Improper input, enter a number and unit if temperature")

def c2f(userInput):
   userTemp = float(userInput)
   CtoF = ((userTemp * (9/5)) + 32) 
   print ("{}°C = {}°F".format(userInput,CtoF))

def f2c (userInput):
   userTemp = float(userInput)
   FtoC = ((userTemp - 32) * (5/9))
   print ("{}°F = {}°C".format(userInput,FtoC))


main()
