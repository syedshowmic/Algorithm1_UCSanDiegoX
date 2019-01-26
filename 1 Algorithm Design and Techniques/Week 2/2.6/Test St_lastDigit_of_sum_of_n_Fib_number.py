# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 02:39:50 2018

@author: st
"""
    
def fib_sum_last_digit(n):
    #using matrix definition of Fibonacci numbers
    # creating a matrix [[1,1],[1,0]]
    a = 1
    b = 1
    c = 0
    FIN.clear()
    for i in range(n, n + 3):
        for z in bin(n)[3:]:
            
            ans = (b*b) % 10
            a, b, c = (a * a + ans) % 10, ((a + c) * b) % 10, (ans + c * c) % 10
            if z == '1': a, b, c = (a+b) % 10, a, b
        FIN.append(b)
    return FIN[0]

FIN = []    
n = (int(input())) 

print(fib_sum_last_digit(n))


if b == 0:
            answer = 9
        else:
            answer = b - 1

m = n + 2

m = (int(input())) 
M  = []
for i in range(m, m + 3):
    
    def fib_last_digit(i):
        v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
        for rec in bin(i)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
            calc = (v2*v2) % 10
            v1, v2, v3 = (v1*v1+calc) % 10, ((v1+v3)*v2) % 10, (calc+v3*v3) % 10
            if rec == '1': v1, v2, v3 = (v1+v2) % 10, v1, v2
            M.append(v2)
        return M
    
    print(M)

print(fib_last_digit(i))
