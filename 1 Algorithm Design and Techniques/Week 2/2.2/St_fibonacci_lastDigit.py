# Uses python3
def calc_fib(n):
    fibonacci_list = [0, 1]
    
    for i in range(2, n + 1):
        fibonacci_list.append(fibonacci_list[-1] + fibonacci_list[-2])
    return fibonacci_list[-1]

n = int(input())
print(str(calc_fib(n))[-1])


# =============================================================================
# last_Number = calc_fib(n) % 10
# print(last_Number)
# =============================================================================
# =============================================================================
# LAST_DIGIT = list(str(calc_fib(n)))
# LAST_NUMBER = LAST_DIGIT[-1]
# =============================================================================
#print(LAST_NUMBER)




# =============================================================================
# newList = list((calc_fib(n)))
# lastNumber = newList[-1]
# print(lastNumber)
# lastDigit = list(str(lastNumber))[-1]
# print(lastDigit)
# =============================================================================

print(calc_fib(n)) #% is modulus operator in python


z = 9827000000000000000000000000

z.split()
