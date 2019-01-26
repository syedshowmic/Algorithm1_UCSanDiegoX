# Uses python3

#n = list(range(2, 2*10**5))





# =============================================================================
# lastItem = int(A[-1])
# last2ndItem = int(A[-2])
# =============================================================================




#def St_max(A):
A = [int(x) for x in input().split()]
n = len(A) - 1
    
for i in A:
    A = sorted(A)
    result = A[n - 1] * A[n]

print(result)
    
    