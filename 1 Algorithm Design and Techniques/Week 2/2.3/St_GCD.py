#uses python3
def gcd(a, b):
    
    if (b == 0):
        return a
    else:
        a2 = a % b
        return gcd(b, a2)


a, b = map(int, input().split())

print(gcd(a, b))
