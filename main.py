"""
Store logic for processing all supported calculator actions
"""

def add(a: int | float, b: int | float) -> int | float:
    return a+b

def subtract(a: int | float, b: int | float) -> int | float:
    return a-b

def multiply(a: int | float, b: int | float) -> int | float:
    return a*b

def divide(a: int | float, b: int | float) -> int | float:
    return a/b

def exponent(a: int|float, power: int|float) -> int | float:
    '''
    Calculates result of a^(power), 
    if power is an integer simply mulitplies a by itself power times 
    (result initially set to 1, i.e a^0 for all a)

    else if power is a float it splits it into its parts (integer and decimal)
    such that a^(power) = a^(int_power) + a^(float_power) it then recursively calls 
    exponent() on the integer portion of the equation and 
    [INSERT EXPLANATION FOR DECIMAL CALCULATION HERE]
    '''
    if power.__class__ != int:
        str_power = str(power)
        int_power = ''  #  Integer part of power
        float_power = ''  #  Decimal/float part of power
        #  splits power into integer and decimal/float parts allowing equation to be split into a^(float: power) = a^(int_power) + a^(float_power)
        for i in range(len(str_power)-1):
            if str_power[i] != '.':
                int_power += str_power[i]
            else:
                float_power = str_power[i+1:]
        int_power = int(int_power)
        ''' result = exponent(a, int_power)  #  Recursive (?) call to exponent that returns the a^(int_power) part of equation
        #  Logic for float/decimal portion goes here
        result += n_root(a, int(float_power))'''

        result = n_root(a * exponent(10, len(float_power)+1), int(float_power))

    else:
        #  Initializes result as a^0 and then multiplies it by a for power times and returns
        result = 1  #  Sets result == a^0 for all a
        for i in range(power):
            result *= a
    
    return result
            

def n_root(a: int|float, n: int|float, precision_value: int = 10) -> int|float:
    '''
    Uses Newton's method with a default repetition of 10 times to 
    approximate a^(1/n) for any a, n in the set of real numbers.
    '''
    approx = 1  #  Sets initial value (a_0_) to equal 1
    for i in range(precision_value):
        approx = (1/n) * ((n-1) * approx + (a / exponent(approx, n-1)))
    
    return approx

def sin_rad(theta: int|float) -> int | float:
    # T B I
    pass

def cos_rad(theta: int|float) -> int | float:
    # T B I
    pass

def tan_rad(theta: int|float) -> int | float:
    # T B I
    pass