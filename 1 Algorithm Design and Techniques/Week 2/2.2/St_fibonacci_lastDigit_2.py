def Last_Digit(n):
    number_1 = 1 
    number_2 = 1
    
    while n > 2:
        temp_number = number_1
        number_1 = number_1 + number_2
        number_2 = temp_number
        n = n - 1

        number_1 %= 10  
        number_2 %= 10
    
    return number_1 if n != 0 else 0



n = int(input())
print(Last_Digit(n))
