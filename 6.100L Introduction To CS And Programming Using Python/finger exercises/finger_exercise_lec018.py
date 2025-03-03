# Write the class according to the specifications below:
class Circle():
    def __init__(self, radius):
        ''' 
        Initializes self with radius.
        '''
        self.radius = radius

    def get_radius(self):
        ''' 
        ---
        #### return:
            radius of self.
        '''
        return self.radius

    def __add__(self, c):
        ''' 
        - c: Circle object.
        ---
        #### return: 
            new Circle object whose radius is the sum of self and c's radius .
        '''
        return Circle(self.radius + c.radius)

    def __str__(self):
        ''' 
        A Circle's string representation is the radius.
        '''
        return str(self.radius)