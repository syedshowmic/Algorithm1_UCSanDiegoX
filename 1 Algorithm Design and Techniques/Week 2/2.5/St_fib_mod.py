#Uses Python3

#Fibonacci Modulus

def fib_mod(n, m):
    
    z = n % m
    def calc_fib(z):
        fibonacci_list = [0, 1]
        
        for i in range(2, z + 1):
            fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
        return fibonacci_list
    
    answer = calc_fib(n)[z] % m
    return answer
    
a = [int(x) for x in input().split()]
n = a[0]
m = a[1]

print(fib_mod(n, m))
