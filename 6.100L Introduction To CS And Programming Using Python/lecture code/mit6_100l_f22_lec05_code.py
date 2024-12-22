#################################################
######################## AT HOME ##########################
#################################################
# 1. If you are incrementing from 0 by 0.022, how many increments 
# can you do before you get a floating point error? 

# x = 0
# count = 20     # check different numbers here
# for i in range(count):
#     x += 0.022 # increment
#     print(x)      # check this value for floating point error


# 2. Automate the code from the previous problem. Suppose you are 
# just given an increment value. Write code that automatically
# determines how many times you can add increment to itself 
# until you start to get a floating point error.

e = 0.022
count = 1
x = e

while x == (e*count):
    x += e
    count += 1

print(f'{count-1}')