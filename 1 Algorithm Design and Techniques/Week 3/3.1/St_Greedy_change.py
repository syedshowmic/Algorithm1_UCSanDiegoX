# Uses python3


def get_change(m):
    get = (m // 10) + ((m % 10) // 5) + (((m % 10) % 5) // 1)
    

    return get

m = int(input())
print(get_change(m))

