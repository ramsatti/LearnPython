array = [7,9,4,0]
min = array[0] 
     
for i in range(0, len(array)):    
   if(array[i] < min):    
       min = array[i]    
           
print("Smallest element present in given array: " + str(min))