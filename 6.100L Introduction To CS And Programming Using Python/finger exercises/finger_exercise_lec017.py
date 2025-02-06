class Circle():
    def __init__(self, radius):
        ''' 
        Initializes self with radius.
        '''
        self.radius = radius

    def get_radius(self):
        '''
        #### Return: 
            radius of self.
        '''
        return self.radius

    def set_radius(self, radius):
        ''' 
        - radius is a number.
        ---
        Changes the radius of self to radius.
        '''
        self.radius = radius

    def get_area(self):
        ''' 
        ---
        #### Return:
            area of self using pi = 3.14.
        '''
        return 3.14 * (self.radius**2)

    def equal(self, c):
        ''' 
        - c is a Circle object.
        ---
        #### Return:
            True if self and c have the same radius value.
        '''
        return self.radius == c.radius

    def bigger(self, c):
        ''' 
        - c is a Circle object.
        ---
        #### Return:
            self or c, the Circle object with the bigger radius.
        '''
        return self if self.radius > c.radius else c