PI = 3.14
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b 

def find_max(*numbers):
    if len(numbers) == 0:
        return None
    
    max_son = numbers[0]
    for son in numbers:
        if son > max_son:             
            max_son = son
    
    return max_son