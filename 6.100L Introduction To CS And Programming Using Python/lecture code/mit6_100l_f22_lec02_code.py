#########################################
############### LECTURE ##########################
#########################################

############## YOU TRY IT ###############

# Write a program that: 
# * Asks the user for a verb.
# * Prints "I can _ better than you" where you replace _ with the verb.
# * Then prints the verb 5 times in a row separated by spaces.
# For example, if the user enters run, you print:
#     I can run better than you!
#     run run run run run
verb = input("verb: ")

print(f"I can {verb} better than you")
print(5*(' '+verb))

#########################################

# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints a bool depending on whether the guess matches the secret.
secret = 17
guess = int(input('guess the number: '))

print(secret == guess)

#########################################

# Buggy
x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))

if x == y:
    print(x,"is the same as",y)
print("These are equal!")
# fix it!
x = int(input("Enter a number for x: "))
y = int(input("Enter a different number for y: "))

if x == y:
    print(x,"is the same as",y)
    print("These are equal!")

#########################################

# Write a program that:
# * Saves a secret number. 
# * Asks the user for a number guess.
# * Prints whether the guess is too low, too high, or the same as the secret. 
secret = 17
guess = float(input('guess the number: '))

if guess > secret:
    print('too high')

elif guess < secret:
    print('too low')

else: 
    print('right number')