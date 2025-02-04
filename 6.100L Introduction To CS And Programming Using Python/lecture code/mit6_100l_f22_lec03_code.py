#########################################
########### YOU TRY IT ##################
#########################################
# Expand this code to show a sad face when the user entered 
# the while loop more than 2 times. Hint: use a counter
#########################################
# where = input("Go left or right? ")
# while where == "right":
#     where = input("Go left or right? ")
# print("You got out!")
n = 0
where = input('go left or right? ')

# While the user chooses 'right', the loop continues
while where == 'right':
    n += 1
    if n > 2:
        print(':(')
    where = input('go left or go right? ')

print('you got out')

#########################################
# Fix this code to use variables start and end in the 
# range, to get the total sum between and including those values. 
# mysum = 0
# start = 3
# end = 5
# for i in range(start, end):
#     mysum += i
# print(mysum)
mysum = 0
start = 3
end = 5

# Iterate through numbers in range
for i in range(start, end+1):
    mysum += i

print(mysum)

#########################################
################ AT HOME ################
#########################################
# Practice 1: 
# Declare a variable x that stores an int > 0. Print all ints, one on each
# line, between 1 (inclusive) and x (inclusive) that are divisible by 5.
# For ex. if x = 15, it prints 5, 10, and 15. 
# For ex. if x = 14, it prints 5 and 10.
x = 14

# Looping through numbers in range from 1 to x
for n in range(1,x+1):
    if n % 5 == 0:
        print(n)

#########################################
# Practice 2:
# Declare a variable n that stores an int. Print the sum of all digits 
# in n. Hint: you can get a digit at a time looking at the remainder 
# when you divide n by 10.
# For ex. If x = 1234, print 10
n = 1234
tot = 0

# Continue looping while 'n' > 0
while n > 0:
    tot += n % 10 
    n //= 10

print(tot)