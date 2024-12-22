################ YOU TRY IT ################
# Write code that loops a for loop over some range 
# and prints how many even numbers are in that range. Try it with:
# range(5)
# range(10)
# range(2,9,3)
# range(-4,6,2)
# range(5,6)
even = 0

for i in range(5):
    if i % 2 == 0:
        even += 1 

print(even)

#############################################

# Assume you are given a string of lowercase letters in variable s. 
# Count how many unique letters there are in s. For example, if 
# s = "abca" Then your code prints 3. 
s = 'abca'
seen = ''

for c in s:
    if c not in seen:
        seen += c

print(len(seen))

##############################################

# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, it doesn't print anything. 
found = False
secret = 4

for i in range(10+1):
    if i == secret:
        found = True
        print(i)

################################################

# Hardcode a number as a secret number. Write a program that 
# checks through all the numbers between 1 to 10 and prints the 
# secret value. If it's not found, prints that it didn't find it.   
found = False
secret = 4

for i in range(10+1):
    if i == secret:
        found = True
        print(i)

if not found:
    print('Not found')

####################################################
##################### AT HOME ######################
######################################################
# Write code that counts how many unique common characters there are between 
# two strings. For example below, the common characters count is 8: 
# text1 = "may the fourth be with you"
# text2 = "revenge of the sixth"
# Hint, start to write your code with a smaller example, then test it on the above text.
text1 = "abc"
text2 = "cde"
count = 0

for c in set(text1 + text2):
    count += 1

print(count)
