# Uses python3
import sys


#Creating optimal value method
def get_optimal_value(capacity, weights, values):
    value = 0.
    
    #Creating List of items
    Frac_ = [float(Vi) / float(wi) for Vi, wi in zip(values, weights)]
    
    #for loop
    for anything in range(len(weights) + 1):
        #if no remaining capacity
        if capacity == 0:
            return value
            break
        #maximum weight
        max_wgt = max(Frac_)
        index = Frac_.index(max_wgt)
        
        #updating value
        Frac_[index] = -1
        Updt_capacity = min(capacity, weights[index])
        value += Updt_capacity * max_wgt
        
        #updated capactity
        weights[index] -= Updt_capacity
        capacity -= Updt_capacity
    
    #return value
    return value

#main function which is provided
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
