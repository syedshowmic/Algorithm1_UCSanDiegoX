#Uses Python 3

n = int(input())
N_Matrix = []

for i in range(n, n + 3):
    
    def fib_last_digit(i):
        a = 1
        b = 1
        c = 0
        for rec in bin(i)[3:]:
            ans = (b*b) % 10
            a, b, c = (a * a + ans) % 10, ((a + c) * b) % 10, (ans + c * c) % 10
            if rec == '1': a, b, c = (a+b) % 10, a, b
        return b
    
    N_Matrix.append(fib_last_digit(i))
    #print(N_Matrix)

#formula Sum of F(n) = F(n+2) - 1
if N_Matrix[-1] == 0:
    answer = 9
else:
    answer = (N_Matrix[-1] - 1)
print(answer)
