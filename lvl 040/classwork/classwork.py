# 1)

def count_sheeps(sheep):
    return sheep.count(True)


# 2)

def no_space(x):
    return x.replace(" ", "")

# 3)

def double_integer(i):
    return i*2


# 4)

def greet(name):
    return "Hello, {} how are you doing today?".format(name)


# 5)

def boolean_to_string(b):
    return str(b)

# 6)
def basic_op(operator, value1, value2):
    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    else:
        return value1 / value2
    

# 7)

def litres(time):
    return int(time * 0.5)


# 8)

def century(year): 
    if year % 100 == 0:
        return year // 100
    else:
        return year // 100 + 1