# Implement the function that meets the specifications below:
def count_sqrts(nums_list):
    '''
    - nums_list: a list.
    ---
    #### Return:
        How many elements in nums_list are exact squares of elements in the same list, including itself.
    ---
    #### Note:
        Assumes that nums_list only contains positive numbers and that there are no duplicates.
    '''
    count = 0
    
    # Loop: iterate over each number in nums_list
    for n in nums_list:
        if n**2 in nums_list:
            count += 1
    
    return count
    
# Examples:    
print(count_sqrts([3,4,2,1,9,25])) # prints 3