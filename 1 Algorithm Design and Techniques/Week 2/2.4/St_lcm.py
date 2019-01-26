#uses python3

def L_C_M(a, b):
    
    #using greatest common divisor to find an important common factor
    def gcd(a, b):
        if (b == 0):
            return a
        else:
            a2 = a % b
            return gcd(b, a2)
    
    #separate conditions for when Greatest common Divisor = 1 and when gcd != 1
    if (gcd(a, b) == 1):
        lcm2 = (a * b)
        return lcm2
    else:
        lcm = gcd(a, b) * (a // gcd(a, b)) * (b // gcd(a, b)) # / sign converts to a float
        return lcm

a, b = map(int, input().split())
print(L_C_M(a, b))
