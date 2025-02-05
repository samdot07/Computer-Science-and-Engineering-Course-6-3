# Assume you are given an integer 0 \<= N \\<= 1000
# Write a piece of Python code that uses bisection search to guess N
# The code prints two lines: 
# count: with how many guesses it took to find N, 
# and answer: with the value of N
# Hints: If the halfway value is exactly in between two integers, choose the smaller one
N = int(input('Choose an integer: '))
count = 0
low = 0
high = 100

guess = (high+low) / 2

# Loop: loop until the guess matches the chosen number
while guess != N:
    if N > guess:
        low = guess
    
    else:
        high = guess
    
    guess = (high+low) / 2
    count += 1

print(count)
print(guess)