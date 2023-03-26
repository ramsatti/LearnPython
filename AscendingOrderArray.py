array = [1,2,3,4]
anotherArray = []
min = array[0] 
     
for i in range(0, len(array)):    
   if(array[i] > min):    
       min = array[i]    
           
print("Largest element present in given array: " + str(min))