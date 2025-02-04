#########################################
########### YOU TRY IT ##################
#########################################
x = 0.5
epsilon = 0.01
# # choose the low endpoint
low = 0
# # choose the high endpopint
high = x

guess = (high + low)/2

# Continue refining the guess until the difference between guess squared and x is less than epsilon
while abs(guess**2 - x) >= epsilon:
    if guess**2 < x:
        low = guess
    
    else:
        high = guess
    
    guess = (high + low)/2.0

print(f'{str(guess)} is close to square root of {str(x)}')

#########################################
# Write code to use bisection search to find the cube 
# root of positive cubes to within some epsilon
cube = 27
epsilon = 0.01
low = 0
high = cube
guess_num = 0

guess = (high+low) / 2.0

# Continue refining the guess until the difference between guess cubed and cube is less than epsilon
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    
    else:
        high = guess 
    
    guess = (high+low) / 2.0
    guess_num += 1

print(guess_num)