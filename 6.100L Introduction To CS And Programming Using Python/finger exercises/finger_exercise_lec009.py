# Implement the function that meets the specifications below:
def dot_product(tA, tB):
    '''
    - tA: a tuple of numbers.
    - tB: a tuple of numbers of the same length as tA.
    ---
    #### return:
        tuple, where the:
            first element is the length of one of the tuples.
            second element is the sum of the pairwise products of tA and tB.
    ---
    #### Note:
        Assume tA and tB are the same length.
    '''
    sum = 0
    
    # Loop: iterate over the range of indices in tA
    for i in range(len(tA)):
        sum += tA[i] * tB[i]
    
    return (len(tA), sum) 

# Examples:
tA = (1, 2, 3)
tB = (4, 5, 6)   
print(dot_product(tA, tB)) # prints (3,32)