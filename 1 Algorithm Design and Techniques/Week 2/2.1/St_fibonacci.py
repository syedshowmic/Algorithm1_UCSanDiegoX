# Uses python3
def calc_fib(n):
    fibonacci_list = [0, 1]
    
    for i in range(2, n + 1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list



n = int(input())
print(calc_fib(n)[n])



