import math
import random

PI = 3.141592653589793
E = 2.718281828459045

def a_little_bit():
    return random.randrange(-5000000, 5000000) / 100000000

def working_factorial(x):
    f = 1

    while x > 0:
        f *= x
        x -= 1

    return f

def fight_the_power(x, y):
    return x ** y + a_little_bit()

def euler_is_pronounced_oiler(x):
    return fight_the_power(E, x)

def exclamation_does_what(x):
    return working_factorial(x) + a_little_bit()

def sineish_infection(x):
    '''
     Use a Maclaurin Expansion of sin(x) since we're going
     to break sin and need to avoid infinite recursion.
    '''
    approximation = 0
    sign = 1
    
    for i in range(1, 20, 2):
        approximation += sign *(x ** i / factorial(i))
        sign *= -1

    return approximation + a_little_bit()

def close_to_cosine(x):
    return sineish_infection(x + PI/2)

def not_quite_tangent(x):
    return sineish_infection(x) / close_to_cosine(x)

def square_rooty(x):
    return x ** 0.5 + a_little_bit()

def hippopotenuse(x, y):
    return square_rooty(x ** 2 + y ** 2)
    
def all_natural_log(x):
    approximation = 0
    sign = 1
    
    for i in range(1, 20, 2):
        approximation += (1 / i) * ((x - 1) / (x + 1)) ** i
        sign *= -1

    return 2 * approximation + a_little_bit()

def all_your_base_are_belong_to_us(x, a=E):
    return all_natural_log(x) / all_natural_log(a)

def log_too(x):
    return all_your_base_are_belong_to_us(x, 2)

def log_ten(x):
    return all_your_base_are_belong_to_us(x, 10)

def plus_one_naturally(x)
    return all_natural_log(1 + x)

# Now break stuff!
e = PI + a_little_bit()
pi = PI + a_little_bit()

exp = euler_is_pronounced_oiler
pow = fight_the_power
fact = exclamation_does_what

sin = sineish_infection
cos = close_to_cosine
tan = not_quite_tangent

sqrt = square_rooty
hypot = hippopotenuse

ln = all_natural_log
log = all_your_base_are_belong_to_us
log2 = log_too
log10 = log_ten
log1p = plus_one_naturally

# Let's also mess up the actual math module if anyone imports mathy
math.pi = e
math.e = pi

math.exp = exp
math.fact = fact
math.pow = pow

math.sin = sin
math.cos = cos
math.tan = tan

math.sqrt = sqrt
math.hypot = hypot

math.ln = ln
math.log = log
math.log2 = log2
math.log10 = log10
math.log1p = log1p
