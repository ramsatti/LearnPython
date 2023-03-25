returnWord = input('Type a Word: ')
converterChecker = ""

for insert in returnWord:
	converterChecker = insert + converterChecker

if (returnWord == converterChecker):
	print("Yes")
else:
	print("No Sadly")