# gets number inputs
num1 = input("Enter number here: ")  
num2 = input("Enter number here: ") 
num3 = input("Enter number here: ")

if num1 > num2:
    if num2 > num3:
        print (num3)
    else: 
        print (num2)
else:
    if num1 > num3:
        print (num3)
    else:
        print (num1)
  
  
