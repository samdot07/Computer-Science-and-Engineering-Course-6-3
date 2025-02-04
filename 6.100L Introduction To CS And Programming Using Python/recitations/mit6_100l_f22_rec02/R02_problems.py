# Practice Problem 1
# Write a program that takes your name as an Input and Outputs the length of your name minus 5.
name = str(input('Write your name: '))

print(len(name) - 5)

#########################################
# Practice Problem 2
# Write a program to remove the nth character from a non empty string.
# Print the old string and the new string.
test_string = "We want to remove the nth character from this string"
n = 8

print(f'Old string: {test_string}\n'
      f'New string: {test_string[:7] + ' ' + test_string[9:]}')

#########################################
# Practice Problem 3
# Write a program which answers the following:
# Does a given string have length greater than 10 or less than 5? If True, output True. If False, output False.
my_string = "This is my string"  # example string - modify to test

print(len(my_string) > 10 or len(my_string) < 5)

#########################################
# Practice Problem 4
# Write a program which answers the following using a for loop:
# Count the number of e's in the following string
my_string = "How many times is the letter e in this string?"

# Iterate through each character in the string
for c in my_string:
    count = my_string.count('e')
    
print(count)