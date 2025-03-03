# Problem Set 4a
from tree import Node # Imports the Node object used to construct trees

# Part A0: Data representation
# Fill out the following variables correctly.
# If correct, the test named test_data_representation should pass.
tree1 = Node(8, 
             Node(2, Node(1), Node(6)), 
             Node(10)
            )
tree2 = Node(7, 
             Node(2, Node(1), 
                  Node(5, Node(3), Node(6))
                 ),
             Node(9, Node(8), Node(10))
            )
tree3 = Node(5,
             Node(3, Node(2), Node(4)),
             Node(14, Node(12),
                  Node(21, Node(20), Node(26)))
            )

def find_tree_height(tree):
    '''
    #### Input:
    - tree: An element of type Node constructing a tree.
    ---
    #### Output:
        The integer depth of the tree.
    ---
    Find the height of the given tree.
    '''
    # Recursion: find the height of the right 
    # and the left subtree
    right_h = find_tree_height(tree.right)
    left_h = find_tree_height(tree.left)
    
    if tree is None:
        return -1
    
    return 1 + max(right_h, left_h)

def compare_func(child_value, parent_value):
    '''
    - child_value: int, value of the child node in the tree. 
    - parent_value: int, value of the parent node in the tree.
    ---
    #### return:
        For max heaps: True if child_value < parent_value, False otherwise. 
    -   For min heaps: True if child_value > parent_value, False otherwise.
    '''
    if child_value < parent_value or child_value > parent_value:
        return True
    
    return False
    
def is_heap(tree, compare_func):
    '''
    #### Inputs:
    - tree: An element of type Node constructing a tree.
    - compare_func: A function that compares the child node value to the parent node value. i.e.
        - op(child_value,parent_value) for a max heap would return True if child_value < parent_value and False otherwise.
        - op(child_value,parent_value) for a min meap would return True if child_value > parent_value and False otherwise.
    ---
    #### Output:
        True if the entire tree satisfies the compare_func function; False otherwise.
    ---
    Determines if the tree is a max or min heap depending on compare_func.
    ''' 
    if tree is None:
        return True
    
    # Loop: iterate over the left and right children of the current node
    for c in [tree.right, tree.left]:
        if c:
            if not compare_func(c.value, tree.value):
                return False
            
            # Recursion: check if the child subtree satisfies the heap property
            if not is_heap(c, compare_func):
                return False

    return True

if __name__ == '__main__':
    # You can use this part for your own testing and debugging purposes.
    # IMPORTANT: Do not erase the pass statement below if you do not add your own code
    pass