# Problem 1:
# For each of the following expressions, what is the order of growth class 
# that best describes it?
# a) 8n                     # O(n) -> linear
# b) 3n**2 + 7n**3 + 4      # O(n**3) -> polynomial
# c) 5log(n) + 5n           # O(n) -> linear
# d) 3**n + n**2            # O(n**2) -> polynomial
# e) 20n + nlog(n)          # O(nlog(n)) -> log-linear
# f) 5 + 60                 # O(1) -> constant
# g) log(n) + 4n            # O(n) -> linear

#########################################
# Problem 2:
# Rank the following functions by runtime complexity. Note some may have 
# the same runtime complexity.
# f(n) = n**2 + 4n + 2                              # 1) h(n) = log2(n), O(log(n)) -> logarithmic
# g(n) = log(n**2)                                  # 2) g(n) = log(n**2), O(log(n)) -> logarithmic
# h(n) = log2(n)  (i.e. read as log base 2 n)       # 3) f(n) = n**2 + 4n + 2, O(n**2) -> polynomial
# j(n) = 3n**3 + 2                                  # 4) j(n) = 3n**3 + 2, O(n**3) -> polynomial
# l(n) = n!                                         # 5) k(n) = 2**n, O(2**n) -> exponential
# k(n) = 2**n                                       # 6) l(n) = n!, O(n!) -> factorial

#########################################
# Problem 3:
# What is the time complexity for the following programs? 

# O(n) -> linear, where
# n = length of 'my_list'
def program1():
    my_list = [1,2,3,4,5,6,7,8]
    my_list_even= []
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_list_even.append(i)
    return my_list

# O(n*m) -> linear, where
# n = length of 'my_list'
# m = length of 'my_second_list'
def program2():
    my_list = [1,2,3,4,5,7]
    my_second_list = [1,2,3,4,5,7]
    
    output_list1 = [i for i in my_list]

    output_list2 = []
    for i in my_list:
        for j in my_second_list:
            output_list2 += [i,j]
    
    return (output_list1, output_list2)

# O(log(n)) -> logarithmic
def program3(n):
    epsilon = 0.01
    low = 0
    high = n
    ans = (high + low) / 2 
    
    while abs(ans**4 - n) >= epsilon:
        if ans**4 > n:
            high = ans 
        else: 
            low = ans
        ans = (high + low) / 2
    return ans

#########################################
# Problem 4:
# Describe two ways to construct an algorithm to find the maximum number in a list. 
# One algorithm should have time complexity O(n), the other O(n**2). (Note the 
# O(n**2) algorithm is highly inefficient and we'd never actually use it 
# in practice).
# time complexity O(n)
def getmax(l):
    '''
    #### return:
        int, maximum number in a list.
    '''
    return max(l)

# time complexity O(n**2)
def getmax_new(l):
    '''
    #### return:
        int, maximum number in a list.
    '''
    # Loop: iterate over each index in range of list 'l'
    for _ in range(len(l)):
        m = max(l)
    return m