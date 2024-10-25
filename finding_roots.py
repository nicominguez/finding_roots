import math

def func(x: float) -> float:
    return x*x*x + x*x - 5*x + 6;
    #return pw_func(x)

def pw_func(x: float) -> float:
    if x<=1: return 0.01*math.sin(x)+1
    elif x>=1: return  0.01*math.sin(x)+1
    else: return 11*(x-1.1)*(x-1.9)

def derivative_at_point(x):
    h = 0.00000000001
    return (func(x + h) - func(x))/h

def bisector(a, b):
    if func(a) * func(b) > 0:
        print("No zero withing bounds.")
        return
    c = 0
    while (b - a) > 0.0001:
        c = (a + b)/2
        if func(c) == 0: break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c

def newton_raphson(x):
    if abs(derivative_at_point(x)) < 0.0001: return newton_raphson(x-0.1)
    d = func(x) / derivative_at_point(x)
    while abs(d) > 0.0001:
        if func(x) == 0:
            break
        x = x - d
        d = func(x) / derivative_at_point(x)
    return x

if __name__ == '__main__':
    print("Value of root: ", bisector(-100, 100))
    print("Value of root: ", newton_raphson(0.99999999))