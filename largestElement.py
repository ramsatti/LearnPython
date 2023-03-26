array = [7,9,4,0]
max = array[0] 
     
for i in range(0, len(array)):    
   if(array[i] > max):    
       max = array[i]    
           
print("Largest element present in given array: " + str(max))