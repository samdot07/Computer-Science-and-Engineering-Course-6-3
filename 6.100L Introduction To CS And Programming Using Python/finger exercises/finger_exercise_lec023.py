# Choose the worst case asymptotic order of growth (upper and lower bound) 
# for the following functions.
# Assume n = a.
# O(n) -> linear
def running_product(a):
    ''' - a: int. '''
    product = 1
    for i in range(5,a+5):
        product *= i
        if product == a:
            return True
    return False
 
#########################################
# Assume n = len(L).
# O(n**2) -> polynomial
def tricky_f(L, L2):
    ''' - L and L2: list, equal length. '''
    inL = False
    for e1 in L:
        if e1 in L2:
            inL = True
    inL2 = False
    for e2 in L2:
        if e2 in L:
            inL2 = True
    return inL and inL2

#########################################
# O(log(n)) -> logarithmic
def sum_f(n):
    ''' n > 0. '''
    answer = 0
    while n > 0:
        answer += n%10
        n = int(n/10)
    return answer