def zero(function = None): 
    if not function:
        return 0
    else:
        return function(0)

def one(function = None): 
    if not function:
        return 1
    else:
        return function(1)

def two(function = None): 
    if not function:
        return 2
    else:
        return function(2)

def three(function = None): 
    if not function:
        return 3
    else:
        return function(3)

def four(function = None): 
    if not function:
        return 4
    else:
        return function(4)

def five(function = None): 
    if not function:
        return 5
    else:
        return function(5)

def six(function = None): 
    if not function:
        return 6
    else:
        return function(6)

def seven(function = None): 
    if not function:
        return 7
    else:
        return function(7)

def eight(function = None): 
    if not function:
        return 8
    else:
        return function(8)
        
def nine(function = None): 
    if not function:
        return 9
    else:
        return function(9)

def plus(y): 
    return lambda x: x+y

def minus(y): 
    return lambda x: x-y

def times(y): 
    return lambda  x: x*y

def divided_by(y): 
    return lambda  x: x//y

print (four(plus(nine()))) # must return 13