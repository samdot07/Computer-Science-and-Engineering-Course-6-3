#########################################
########### YOU TRY IT ##################
#########################################
# Write code that satisfies the following specification:
def div_by(n, d):
    ''' 
    - n and d are ints > 0.
    ---
    #### Returns:
        True if d divides n evenly and False otherwise.
    '''
    return n % d == 0

# For example: 
print(div_by(10,3))     # print False
print(div_by(195,13))   # returns True

#########################################

# Write code that satisfies the following specification:
# Hint, use paper and pen for a strategy before coding!
def is_palindrome(s):
    '''
    - s is a string.
    ---
    #### Returns:
        True if s is a palindrome and False otherwise.
    '''
    return s[::] == s[::-1]

#########################################
################ AT HOME ################
#########################################
# 1. Write code that satisfies the following specs:
def keep_consonants(word):
    ''' 
    - word is a string of lowercase letters.
    ---
    #### Returns:
        string, containing only the consonants of word in 
        the order they appear.
    '''
    vowels = 'aeiou'
    
    # Iterate over each character in the word
    for i in word:
        if i in vowels:
            return word.strip(i)

# For example
print(keep_consonants("abcd"))  # prints bcd
print(keep_consonants("aaa"))  # prints an empty string
print(keep_consonants("babas"))  # prints bbs

#########################################

# 2. Write code that satisfies the following specs:
def first_to_last_diff(s, c):
    ''' 
    - s is a string.
    - c is single character string.
    ---
    #### Returns:
        The difference between the index where c first
        occurs and the index where c last occurs.
    ---
    #### Note:
    If c does not occur in s, returns -1. 
    '''
    if c not in s:
        return s.find(c)
        
    return abs(s.find(c) - s.rfind(c))

# For example
print(first_to_last_diff('aaaa', 'a'))  # prints 3
print(first_to_last_diff('abcabcabc', 'b'))  # prints 6
print(first_to_last_diff('abcabcabc', 'b'))  # prints -1