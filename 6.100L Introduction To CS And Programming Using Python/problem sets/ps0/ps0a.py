import numpy

x = float(input('Please enter a number x: '))
y = float(input('Please enter a number y: '))

# Compute power and log
pow = x ** y
log = numpy.log2(x)

print(pow, log)