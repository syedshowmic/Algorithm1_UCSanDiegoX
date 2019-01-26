# Uses python3

#import sys and np
import numpy as np
import sys

#given def
def edit_distance(s, t):
    Val1 = np.zeros(shape = (len(s) + 1, 
                             len(t) + 1), 
                             dtype = int)

    for anything in range(len(s) + 1):
        Val1[anything, 0] = anything
    
    
    for anything in range(len(t) + 1):
        Val1[0, anything] = anything

    for anything in range(1, len(s) + 1):
        for something in range(1, len(t) + 1):
            if s[anything - 1] == t[something - 1]:
                Val1[anything, something] = Val1[anything - 1, something - 1]
            else:
                Val1[anything, something] = 1 + min(Val1[anything - 1, something], 
                                                    Val1[anything - 1, something - 1], 
                                                    Val1[anything, something - 1])
    
    #return cmd
    return (Val1[len(s), len(t)])


if __name__ == "__main__":
    input = sys.stdin.read()
    input = list(map(str, input.split('\n')))
    print(edit_distance(input[0], input[1]))
