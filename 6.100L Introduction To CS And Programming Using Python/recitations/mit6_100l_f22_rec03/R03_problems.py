# Problem 1 - Bisection Search Practice
# Write a program using bisection search to find the fourth root of a number inputted by the 
# user. Print the fourth root calculated with max error of 0.01. 
x = float(input("Using bisection search calculate the forth root of: " ))
epsilon = 0.01
low = 0
high = x

ans = (high+low) / 2.0

# Loop until the answer is within the specified error tolerance
while abs(ans**4 - x) >= epsilon:
    if  ans**4 < x:
        low = ans
    
    else:
        high = ans
    
    ans = (high+low) / 2.0
    
print(ans)

#########################################
# Problem 2 - Functions 
# Write a Python function to check whether a number falls in a given range. 
def inrange(x, n):
    return x in range(n + 1)

print(inrange(0, 10))

#########################################
# Problem 3 - Functions 
# Write a Python function to check whether a number is perfect or not.
# (In number theory, a perfect number is a positive integer that is equal 
# to the sum of its proper positive divisors, excluding the number itself).
# by definition all pefect numbers are even
def isperfect(x):
    return ('Perfect number' if x % 2 == 0 else 'Not a perfect number')

print(isperfect(26))

#########################################
# Problem 4 - Approximation Algorithm (see Lecture 5 slides for similar problem)
# Write an approximation algorithm to calculate the fourth root of some 
# number inputted by the user. 
# Print the result and the number of iterations required to reach that result. 
# The program should not accept negative numbers. Initial parameters epsilon 
# (i.e. accuracy), initial guess, increment and num_guesses are defined below.
# example initial parameters
x = float(input('Choose a positive number: '))
epsilon = 0.01
ans = 0.0
increment = 0.001
num_guesses = 0

# Loop to ensure the user inputs a positive number
while x < 0:
    x = float(input('Choose a positive number: '))

# Loop to approximate the fourth root using incremental guesses
while abs(ans**4 - x) >= epsilon:
    ans += increment
    num_guesses += 1

print(f'The result is: {ans}\n'
      f'It took {num_guesses} guesses')