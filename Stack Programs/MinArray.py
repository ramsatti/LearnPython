array = [1,2,3,4]
max = array[0] 
     
for i in range(0, len(array)):    
   if(array[i] < max):    
       max = array[i]    
           
print("Smallest number = [" + str(max) + "]")