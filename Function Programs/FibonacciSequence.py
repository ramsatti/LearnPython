def fibonacciSequence(num):
    a1 = 0
    a2 = 1
    fibanacciSeq = []
    
    for i in range(0, num):
        fibanacciSeq.append(a1)
        a1, a2 = a2, a1 + a2
    return fibanacciSeq

num = int(input('Write a1 number: '))
print(fibonacciSequence(num))