# Assume you are given a positive integer variable named N
# Write a piece of Python code that finds the cube root of N
# The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube
# Hint: use a loop that increments a counter—you decide when the counter should stop
N = int(input('Choose a positive int: '))
guess = 0
cube_root = guess**(1/3)

# Increment guess until its cube is greater than or equal to N
while guess**3 < N:
    guess += 1

if  guess**3 == N:
    print(guess)
else:
    print('Error')