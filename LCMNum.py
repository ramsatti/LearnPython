def LCMFind(n1, n2): #12, 9
    if n1 > n2:
        n1, n2 = n2, n1 #9, 12
    for x in range(n2, n1 * n2 + 1, n2):# 12, 108, 12 # range(12, 12 * 9 + 1, 12) # [12, 12 *2, 12 *3, ....., 12 *9]
        if x % n1 == 0:
            return (x)

n1 = int(input('n1 = '))
n2 = int(input('n2 = '))
        
lcm = LCMFind(n1, n2)
print('Lcm = ', lcm)