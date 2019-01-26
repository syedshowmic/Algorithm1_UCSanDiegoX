# Uses python3
import sys

def binary_search(a, x):
    low, high = 0, len(a)-1
    return binary_search_repeat(a, low, high, x)

def binary_search_repeat(A, low, high, key):    
    if high < low:
        return - 1
    mid = low + int((high - low) / 2)
    
    if key == a[mid]:
        return mid
    elif key < a[mid]:
        return binary_search_repeat(A, low, mid - 1, key)
    else:
        return binary_search_repeat(A, mid + 1, high, key)


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')