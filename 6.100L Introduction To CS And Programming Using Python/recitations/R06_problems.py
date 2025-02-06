# Problem 1: List concatenation
original_list = [1, 2, 35, 10, 5, 8, 9, 23]

# a) Using List concatenation create a new list from the orignal list, 
# removing all multiples of 5 from a list of numbers.
# expected output: [1, 2, 8, 9, 23]
# Loop: iterate over each element in 'original_list'
new_list = [e for e in original_list if e % 5 != 0]
print(new_list)

# b) Using list concatenation create a new list from the original list, 
# where each element is half the original element
# Expected output: [0.5, 1.0, 17.5, 5.0, 2.5, 4.0, 4.5, 11.5]
# Loop: iterate over each element in 'original_list'
new_list = [e / 2 for e in original_list]
print(new_list)

#########################################
# Problem 2: Write a Function to insert a specified element x in a given list 
# after every nth element.
# Return the new list. 
# Example
# Original list:
# [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
# Insert 20 in list after every 4th element:
# [1, 3, 5, 7, 20, 9, 11, 0, 2, 20, 4, 6, 8, 10, 20, 8, 9, 0, 4, 20, 3, 0]
def insert_element_list1(lst, x, n):
    '''
    - lst: list, input list.
    - x: int, element to insert.
    - n: int, x will be inserted after every nth element.
    ---
    #### Return: 
        new modified list.
    '''
    # Loop: iterate over the list in reverse to avoid affecting indices of unprocessed elements
    for e in range(len(lst) - 1, -1, -1):
        if (e + 1) % n == 0:
            lst.insert(e + 1, x)
    return lst

# testing
nums = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]
x = 20
n = 4
print(insert_element_list1(nums, x, n))

#########################################
# Problem 3: Write a Function to sort list of lists containing integers such that the 
# sub-lists are sorted in increasing order. How would you sort in decreasing order?
# Example:
# Original list of tuples:
# [[10, 10.12, 10.11], [5, 5.3, 4.9], [2.4, 2.6, 2.2]]
# Expected output:
# [[10, 10.11, 10.12], [4.9, 5, 5.3], [2.2, 2.4, 2.6]]
def sort_list_of_lists(lst):
    '''
    - lst: lst, input list.
    - n: int, index to sort by.
    ---
    #### Return: 
        the sorted list.
    '''
    return sorted(lst, reverse=True)

# testing
items = [[10, 10.12, 10.11], [5, 5.3, 4.9], [2.4, 2.6, 2.2]]
print(sort_list_of_lists(items))

#########################################
# Problem 4: Write a Function to split a given list into size n chunks 
# using list comprehension. If the list does not divide equally, the last 
# chunk should be short. Return the new list. 
# Example:
# Original list:
# [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Split the list into equal size 4
# [[12, 45, 23, 67], [78, 90, 45, 32], [100, 76, 38, 62], [73, 29, 83]]
# Split the list into equal size 5
# [[12, 45, 23, 67, 78], [90, 45, 32, 100, 76], [38, 62, 73, 29, 83]]
def split_list(lst, n):
    '''
    - lst: list, input list.
    - n: int, size of chunks.
    #### Return: 
        new split list.
    '''
    # Loop: iterate over the list from 0 to the length of the list in steps of n
    return [lst[e: e+n] for e in range(0, len(lst), n)]

# testing
nums = [12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
n = 4
print(split_list(nums, n))
n = 5
print(split_list(nums,n))