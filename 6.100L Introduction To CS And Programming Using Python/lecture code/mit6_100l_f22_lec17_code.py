#########################################
################ AT HOME ################
#########################################
# Question 1:
# Write a class definition for a vehicle. A vehicle is defined by attributes:
# Number of wheels
# Number of occupants
# Color 
# Decide the type of each data attribute and document this
class vehicle(object):
    '''
    - w: int, number of wheels.
    - o: int, number of occupants.
    - c: string, color of vehicle.
    ---
    Class definition with attributes for a vehicle.
    '''
    def __init__(self, w, o, c):
        self.wheel = w
        self.occupant = o
        self.color = c

#########################################
# Question 2:
# Create 2 vehicle instances using the class we wrote previously. 
# One red vehicle with 2 wheels, and 1 occupant
# One green vehicle with 18 wheels, and 3 occupants
# Print the first one's number of occupants
# Print the second one's color

# red_v = vehicle(2, 1, 'red')
# green_v = vehicle(18, 3, 'green')
# print(red_v.occupant) # prints 1
# print(green_v.color) # prints 'green'

#########################################
# Question 3:
# Add on to the code from above for class Vehicle.
# Create another method for the vehicle class named add_n_occupants, 
# which takes in an int n. When called, self's number of occupants 
# increases by n. It returns the total occupants after the increase. 
    def add_n_occupants(self, n):
        '''
        - n: int, increase in number of occupants.
        ---
        #### Return:
            int, total number of occupants after increase.
        '''
        return self.occupant + n
        
v1 = vehicle(4,2,'blue')
print(v1.occupant)   # prints 2
print(v1.add_n_occupants(3))   # prints 5
print(v1.occupant)

#########################################
# Question 4:
# Add another data attribute to the Vehicle class, called max_occupancy,
# which is always 5. This attribute is not passed in as a parameter, but 
# is defined in the init.
# Modify the add_n_occupants methods such that if adding the occupants 
# exceeds the max_occupancy allowed for that vehicle, 
#   * you do not perform the increase, and
#   * you raise a ValueError with an apprpriate message
class vehicle(object):
    '''
    - w: int, number of wheels.
    - o: int, number of occupants.
    - c: string, color of vehicle.
    ---
    Class definition with attributes for a vehicle.
    
    ---
    #### Note:
        max_occupancy: int, always 5. Not passed as parameter.
    '''
    def __init__(self, w, o, c):
        self.wheel = w
        self.occupant = o
        self.color = c
        self.max_occupancy = 5
        
    def add_n_occupants(self, n):
        '''
        - n: int, increase in number of occupants.
        ---
        #### Return:
            int, total number of occupants after increase.
        '''
        if self.occupant + n <= self.max_occupancy:
            return self.occupant + n
        
        raise ValueError('Max occupancy exceeded')

v1 = vehicle(4,2,'blue')
print(v1.occupant)   # prints 2
print(v1.add_n_occupants(3))   # prints 5
print(v1.occupant)

#########################################
#Question 5:
# Modify the Vehicle class __init__ such that if a vehicle is created
# without specifying a color then the color is set to "black".
# Hint: remember default parameters?
class vehicle(object):
    '''
    - w: int, number of wheels.
    - o: int, number of occupants.
    - c: string, color of vehicle.
    ---
    Class definition with attributes for a vehicle.
    
    ---
    #### Note:
        max_occupancy: int, always 5. Not passed as parameter.
    '''
    def __init__(self, w, o, c='black'):
        self.wheel = w
        self.occupant = o
        self.color = c
        self.max_occupancy = 5