#input ram
#output mar

phrase = "ram" #input('Type a phrase: ')
reversedPhrase = ''

for i in range(len(phrase)-1, -1, -1):
    print('i = ', i)
    reversedPhrase += (phrase[i])

print(reversedPhrase)