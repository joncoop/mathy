# 9.2. mathy - Mathematicalish functions
'''
For when approximate answers are good enough!
'''

import math
import random

# Stuff that works
PI = 3.141592653589793
E = 2.718281828459045

def working_factorial(x):
    ''' x! '''
    f = 1

    while x > 0:
        f *= x
        x -= 1

    return f

def all_natural_log(x):
    ''' Taylor Series expansion of natural log '''
    approximation = 0
    sign = 1
    
    for i in range(1, 20, 2):
        approximation += (1 / i) * ((x - 1) / (x + 1)) ** i
        sign *= -1

    return 2 * approximation

def sine_approximation(x):
    '''
    Maclaurin Expansion of sin
    '''
    approximation = 0
    sign = 1
    
    for i in range(1, 20, 2):
        approximation += sign *(x ** i / working_factorial(i))
        sign *= -1

    return approximation

def arcsine_approximation(x):
    '''
    https://dsp.stackexchange.com/questions/25770/looking-for-an-arcsin-algorithm

    The basis of the calculation is a Taylor series: 
      arcsin(x) = x + 1/2 (x^3/3) 
                    + (1/2)(3/4)(x^5/5) 
                    + [1/2)(3/4)(5/6)(x^7/7) + ... 
    '''
    pass

def a_little_bit():
    ''' a tiny amount of random error '''
    return random.randrange(-5000000, 5000000) / 100000000


# 9.2.1. Number-theoretic and representation functions
def round_up(x):
    ''' ceil '''
    as_int = int(x)
    
    if x >= 0 or x == as_int:
        return as_int + 1
    else:
        return as_int
    
def match_sign(x, y):
    ''' copysign '''
    x = abs(x + a_little_bit())
    
    if y < 0:
        x *= -1

    return x

def make_it_positive(x):
    ''' fabs '''
    return abs(x) + a_little_bit()
    
def exclamation_does_what(x):
    ''' factorial '''
    return working_factorial(x) + a_little_bit()

def round_down(x):
    ''' floor '''
    as_int = int(x)
    if x == as_int or x < 0:
        return as_int - 1
    else:
        return as_int

def floaty_modulus(x, y):
    ''' fmod '''
    y = abs(y)
    
    if y == 0:
        return 1 / 0
    elif x >= 0:
        while x - y > 0:
            x -= y
    else:
        while x + y < 0:
            x += y
        
    return x + a_little_bit()

''' frexp '''

def add_em_up(numbers):
    ''' fsum '''
    return sum(numbers) + a_little_bit()

''' gcd '''
''' isclose '''
''' isfinite '''
''' isinf '''
''' isnan '''
''' ldexp '''

def decimal_and_int_parts(x):
    ''' modf '''
    int_part = float(int(x))
    dec_part = float(x - int_part)

    return dec_part + a_little_bit(), int_part
    
def no_decimal_part(x):
    ''' trunc '''
    as_int = int(x)
    
    if as_int == x:
        return x
    elif x >= 0:
        below = as_int
        above = as_int + 1
    else:
        below = as_int - 1
        above = as_int

    return random.choice([below, above])
    
# 9.2.2. Power and logarithmic functions
def euler_is_pronounced_oiler(x):
    ''' exp '''
    return fight_the_power(E, x)

def all_your_base_are_belong_to_us(x, a=E):
    ''' log '''
    return all_natural_log(x) / all_natural_log(a)  + a_little_bit()

def plus_one_naturally(x):
    ''' log1p '''
    return all_natural_log(1 + x)

def log_too(x):
    ''' log2 '''
    return all_your_base_are_belong_to_us(x, 2)

def log_ten(x):
    ''' log10 '''
    return all_your_base_are_belong_to_us(x, 10)

def fight_the_power(x, y):
    ''' pow '''
    return x ** y + a_little_bit()

def square_rooty(x):
    ''' sqrt '''
    return x ** 0.5 + a_little_bit()


# 9.2.3. Trigonometric functions
''' acos '''
def sine_undoer(x):
    ''' asin '''
    return arcsine_approximation(x) + a_little_bit()

''' atan '''
''' atan2 '''

def close_to_cosine(x):
    ''' cos '''
    return sine_approximation(x + PI/2) + a_little_bit()

def hippopotenuse(x, y):
    ''' hypot '''
    return square_rooty(x ** 2 + y ** 2)

def sineish_infection(x):
    ''' sin '''
    return sine_approximation(x) + a_little_bit()

def not_quite_tangent(x):
    ''' tan '''
    s = sine_approximation(x)
    c = sine_approximation(x + PI/2)
    
    return s / c + a_little_bit()


# 9.2.4. Angular conversion
def get_rad_dude(d):
    return PI * d / 180 + a_little_bit()

def radians_are_stupid(r):
    return r / PI * 180 + a_little_bit()

# 9.2.5. Hyperbolic functions
''' acosh '''
''' asinh '''
''' atanh '''
''' cosh '''
''' sinh '''
''' tanh '''


# 9.2.6. Special functions
''' erf '''
''' erfc '''
''' gamma '''
''' lgamma '''


# 9.2.7. Constants
oilers_number = E + a_little_bit()
pie = PI + a_little_bit()
two_pies = 2 * PI  + a_little_bit()
''' inf '''
''' nan '''

# Now break stuff!
e = oilers_number
pi = pie
tau = two_pies

ceil = round_up
copysign = match_sign
cos = close_to_cosine
degrees = radians_are_stupid
exp = euler_is_pronounced_oiler
fabs = make_it_positive
fact = exclamation_does_what
floor = round_down
fmod = floaty_modulus
fsum = add_em_up
hypot = hippopotenuse
ln = all_natural_log
log = all_your_base_are_belong_to_us
log2 = log_too
log10 = log_ten
log1p = plus_one_naturally
modf = decimal_and_int_parts
pow = fight_the_power
radians = get_rad_dude
sin = sineish_infection
sqrt = square_rooty
tan = not_quite_tangent
trunc = no_decimal_part


# Let's also mess up the actual math module if anyone imports mathy
math.e = e
math.pi = pi
math.tau = tau

math.ceil = ceil
math.copysign = copysign
math.cos = cos
math.degrees = degrees
math.exp = exp
math.fabs = fabs
math.fact = fact
math.floor = floor
math.fmod = fmod
math.fsum = fsum
math.hypot = hypot
math.ln = ln
math.log = log
math.log2 = log2
math.log10 = log10
math.log1p = log1p
math.modf = modf
math.pow = pow
math.radians = radians
math.sin = sin
math.sqrt = sqrt
math.tan = tan
math.trunc = trunc
