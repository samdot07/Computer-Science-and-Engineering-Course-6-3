# Assume you are given a string variable named my_str
# Write a piece of Python code that prints out a new string containing the even indexed characters of my_str
# For example, if my_str = "abcdefg" then your code should print out aceg
my_str = input('Write something: ')

new_str = my_str[::2]
print(new_str)