import numpy as np

def second_largest(arr):
    np_arr = np.array(arr)
    unique_elements = np.unique(np_arr)
    if len(unique_elements) < 2:
        return None
    return np.partition(unique_elements, -2)[-2]

# Test cases
print(second_largest([1, 3, 4, 5, 0, 2]))  
print(second_largest([5, 5, 5, 5, 5]))    
print(second_largest([10, 20]))            
print(second_largest([7]))              
print(second_largest([-1, -3, -2]))       