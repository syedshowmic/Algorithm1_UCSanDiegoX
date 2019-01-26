def Last_Digit(m):
    number_1 = 1 
    number_2 = 1
    
    while m > 2:
        temp_number = number_1
        number_1 = number_1 + number_2
        number_2 = temp_number
        m = m - 1

        number_1 %= 10  
        number_2 %= 10
    
    return (number_1 - 1 ) if m != 0 else 0



n = int(input())
m = n + 2
print(Last_Digit(m))
