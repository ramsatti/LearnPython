def recFactorial(numbuh):  
   if numbuh == 1:  
       return numbuh  
   else:  
       return numbuh*recFactorial(numbuh-1)
   
num = int(input("Enter a number: "))  

if num < 0:  
   print("Sorry, factorial does not exist for negative numbers")  
elif num == 0:  
   print("The factorial of 0 is 1")  
else:  
   print("The factorial of",num,"is",recFactorial(num))  