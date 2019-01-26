# Uses python3
import sys

def get_change(m):
    
    #greedyMin = ((m // 4) + ((m % 4) // 3) + (((m % 4) % 3) // 1))
    #specialMin = (((m - 4) // 4) + ((m - (4 * ((m - 4) // 4))) // 3))
    '''
    the secret for this algorithm is through the coin set (1, 3, 4)
    the highest value coin is 4, so it helps us explore m mod 4, and there is no swifter
    way to get m mod 4 = 0 than to operate m // 4
    similarly we operate for m mod 4 = 1, where m // 4 is 1 short and we add 1, since 1 
    is a valid coin value
    for m mod 4 = 3, we operate m // 4 and then we are short by 3, so we add 1 instance of 3
    finally m mod 4 = 2 is the trickiest, since m // 4 and then adding 2 (1 + 1) is not optimal
    the optimal way is to subtract 4 from m and then use (m - 4) // 4, now we are left with
    4 + 2 = 6 (// 3 = 2); thus we only add 2 instances of 3 valued coins
    '''
    
    if m == 1:
        MinNumCoins = 1
    elif m == 2:
        MinNumCoins = 2
    elif (m % 4 == 0):
        MinNumCoins = m // 4
    elif (m % 4 == 1):
        MinNumCoins = (m // 4) + 1
    elif (m % 4 == 3):
        MinNumCoins = (m // 4) + 1
    elif (m % 4 == 2):
        MinNumCoins = ((m - 4) // 4) + 2
        
    return MinNumCoins

'''
elif (m % 4 != 0) and (m % 3 == 0):
        MinNumCoins = min((m//3), greedyMin)
    elif (m % 4 != 0) and (m % 3 != 0) and (m % 4 == 2):
        MinNumCoins = min(greedyMin, specialMin)
    else:
        MinNumCoins = greedyMin
'''    

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))