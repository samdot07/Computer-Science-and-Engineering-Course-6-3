#########################################
########### YOU TRY IT ##################
#########################################
# Add code to the init method to check that 
# * the type of center is a Coordinate obj and 
# * the type of radius is an int. 
# If either are not these types, raise a ValueError.
class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
        
        if not isinstance(center, Coordinate) or not isinstance(radius, int):
            raise ValueError

center = Coordinate(2, 2)
my_circle = Circle(center, 2)   # no error

my_circle = Circle(2, 2)    # raises ValueError
my_circle = Circle(center, 'two')  # raises ValueError

#########################################
# Implement the missing get_inverse and invert methods below
class SimpleFraction(object):
    ''' 
    A number represented as a fraction.
    '''
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    
    def get_inverse(self):
        ''' 
        ---
        #### return:
            float, representing 1/self.
        ---
        '''
        return 1 / self.num
    
    def invert(self):
        ''' 
        ---
        #### return
            None.
        ---
        Sets self's num to denom and vice versa. 
        '''
        (self.num, self.denom) = (self.denom, self.num)
        
f1 = SimpleFraction(3,4)
print(f1.num, f1.denom)   # prints 3 4 
print(f1.get_inverse())   # prints 1.33333333 (note this one returns value)
f1.invert()               # acts on data attributes internally, no return
print(f1.num, f1.denom)   # prints 4 3 

#########################################
# Modify the str method to represent the Fraction as just the
# numerator, when the denominator is 1. Otherwise its
# representation is the numerator then a / then the denominator.
class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        
        return str(self.num) + "/" + str(self.denom)

# Example:
a = Fraction(1,4)
b = Fraction(3,1)
print(a) # prints 1/4
print(b) # prints 3

#########################################
# Modify the code to return a Fraction object when denominator is 1
class Fraction(object):
    def __init__(self, num, denom):
        '''
        - num, int.
        - denom, int.
        '''
        self.num = num
        self.denom = denom
    
    def reduce(self):
        def gcd(n, d):
            while d != 0:
                (d, n) = (n%d, d)
            return n
        
        if self.denom == 0:
            return None
        
        elif self.denom == 1:
            # modify this
            return Fraction(self.num, 1)
        
        else:
            greatest_common_divisor = gcd(self.num, self.denom)
            top = int(self.num/greatest_common_divisor)
            bottom = int(self.denom/greatest_common_divisor)
            return Fraction(top, bottom)
    
    def __str__(self):
        ''' 
        #### return:
            string, representation of self.
        '''
        # Note this is not the version with the numerator 
        # only when the denomiator is 1
        return str(self.num) + "/" + str(self.denom)
    
f1 = Fraction(5,1)
f1r = f1.reduce()
print(f1r)          # prints 5/1 not 5
print(type(f1r))    # prints <class '__main__.Fraction'>

#########################################
################ AT HOME ################
#########################################
#Question 1.
# Add a method to the Circle class that allows you to print a Circle object
# (you decide how to best represent it!)
class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
    
        if not isinstance(center, Coordinate) or not isinstance(radius, int):
            raise ValueError
    
    def __str__(self):
        return f'{self.center}, {self.radius}'

center = Coordinate(2, 2)
my_circle = Circle(center, 5)
print(my_circle)

#########################################
#Question 2.
# Implement a method in Fraction class such that the operator ** works
# print(a**b) # works after you define it on two Fraction objects
class Fraction(object):
    def __init__(self, num, denom):
        self.num = num
        self.denom = denom
    
    def __float__(self):
        return self.num / self.denom
    
    def __str__(self):
        if self.denom == 1:
            return str(self.num)
        return str(self.num) + "/" + str(self.denom)
    
    def __pow__(self, oth):
        return float(self) ** float(oth)
        
f1 = Fraction(4,1)
f2 = Fraction(1,2)
print(f1, f2)    # prints 2.0
