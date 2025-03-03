# Implement the function that meets the specifications below:
def same_chars(s1, s2):
    '''
    - s1 and s2 are strings.
    ---
    #### return:
        boolean, True if a character in s1 is also in s2, and vice versa.  
    ---
    #### Note:  
        If a character only exists in one of s1 or s2, returns False.
    '''
    return set(s1) == set(s2)

# Examples:
print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False