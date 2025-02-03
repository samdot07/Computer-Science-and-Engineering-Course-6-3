#########################################
################ AT HOME ################
#########################################
# 2. Automate the code from the previous problem. Suppose you are 
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.
e = 0.022
count = 1
x = e

# Loop until 'x' equals 'e * count'
while x == (e*count):
    x += e
    count += 1

print(f'{count-1}')