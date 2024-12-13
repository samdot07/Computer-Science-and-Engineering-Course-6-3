##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input('What is your inital deposit: '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_the_house = 800000
down_payment = cost_of_the_house * 0.25
months = 0
epsilon = 100
low = 0
high = 800000
num_guess = 0

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
# Continue adjusting guess until the absolute difference between 
# the estimated savings and the down payment is within epsilon
# Calculate the amount saved over 'months'
guess = (low + high) / 2.0

# Loop until the absolute difference between the estimated payment and 
# the actual cost is within epsilon tolerance
while abs(down_payment*guess - cost_of_the_house) <= epsilon:
    months += 1
    amount_saved = initial_deposit * (1 + (guess/12)**(months))
    if amount_saved < down_payment:  
        low = guess
    
    else:
        high = guess
    guess = (low + high) / 2.0
    num_guess += 1

print(num_guess)
print(guess)

################
## Test cases ##
################
# Test Case 1
# Enter the initial deposit: 65000
# Best savings rate: 0.380615234375 [or very close to this number]
# Steps in bisection search: 12 [or very close to this number]

# Test Case 2
# Enter the initial deposit: 150000
# Best savings rate: 0.09619140625 [or very close to this number]
# Steps in bisection search: 11 [May vary based on how you implemented your bisection search]

# Test Case 3
# Enter the initial deposit: 1000
# Best savings rate: None
# Steps in bisection search: 0 [May vary based on how you implemented your bisection search]