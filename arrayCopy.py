array1 = input('Type Numbers (Ex: 1,2,3): ')
array2 = [None] * len(array1)
lenArray1 = len(array1)    
     
for insert in range(0, lenArray1):    
    array2[insert] = array1[insert]     
     
print("Elements of original array: ")    
for insert in range(0, lenArray1):    
   print(array1[insert])   
         
print("Elements of new array: ")    

for insert in range(0, lenArray1):    
   print(array2[insert])