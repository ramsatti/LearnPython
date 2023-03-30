punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''  
myString = input("Enter a string: ")  
noPuncuation = ""  

for i in myString:  
   if i not in punctuation:  
       noPuncuation = noPuncuation + i  

print(noPuncuation)  