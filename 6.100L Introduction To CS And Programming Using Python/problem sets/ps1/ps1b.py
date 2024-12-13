##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
year_salary = float(input('What is your year salary: '))
portion_saved = float(input('What is the portion of salary to be saved (decimal): '))
cost_of_dream_home = float(input('What is the cost of your dream home: '))
semi_annual_raise = float(input('What is the semi-annual salary raise (decimal): '))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
down_payment_percentage = 0.25
r = 0.05
amount_saved = 0
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
month_salary = year_salary / 12
down_payment = cost_of_dream_home * down_payment_percentage

# Loop until the total amount saved is greater than or equal to the down payment
while amount_saved < down_payment:
    months += 1
    amount_saved += amount_saved * (r/12)
    amount_saved += portion_saved * month_salary
    if months % 6 == 0:
        month_salary *= (1 + semi_annual_raise)

print(months)
 
################
## Test cases ##
################
# Test Case 1
# Enter your starting yearly salary: 110000
# Enter the percent of your salary to save, as a decimal: .15
# Enter the cost of your dream home: 750000
# Enter the semi-annual raise, as a decimal: .03
# Number of months: 92

# Test Case 2
# Enter your starting yearly salary: 350000
# Enter the percent of your salary to save, as a decimal: .3
# Enter the cost of your dream home: 10000000
# Enter the semi-annual raise, as a decimal: .05
# Number of months: 131