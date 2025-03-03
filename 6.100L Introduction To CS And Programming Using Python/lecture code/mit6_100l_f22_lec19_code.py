#########################################
########### YOU TRY IT ##################
#########################################
# Write a function that meets this spec.
def make_animals(L1, L2):
    ''' 
    - L1 is a list if ints.
    - L2 is a list of str.
    L1 and L2 have the same length.
    ---
    Creates a list of Animals the same length as L1 and L2.
    An animal object at index i has the age and name
    corresponding to the same index in L1 and L2, respectively. 
    '''
    newlist = []
    
    # Loop: iterate over each index in the length of L1
    for i in range(len(L1)):
        name = L1[i]
        age = L2[i]
        a = Animal(age)
        a.set_name(name)
        newlist.append(a)
        
    return newlist

L1 = [2,5,1]
L2 = ["blobfish", "crazyant", "parafox"]
animals = make_animals(L1, L2)
# print(animals)     # note this prints a list of animal objects
for i in animals:  # this prints the indivdual animals
    print(i)
    
#########################################
class Rabbit(Animal):
    ''' A subclass of Animal '''
    def speak(self):
        '''
        ---
        #### return:
            string, prints 'meep' to the console 
        '''
        print('meep')

    def __str__(self):
        ''' 
        Repr as "rabbit", a colon, self's name, a colon, self's age 
        '''
        return "rabbit:"+str(self.get_name())+":"+str(self.get_age())
   
r = Rabbit(5)
print(r)
r.speak()
r.set_name('fluffy')
print(r)
    
#########################################
def make_pets(d):
    ''' 
    - d is a dict mapping a Person obj to a Cat obj.
    ---
    Prints, on each line, the name of a person, 
    a colon, and the name of that person's cat.
    '''
    # Loop: iterate over each [key:value] pair in dict
    for k, v in d.items():
         print(f'{k.get_name()}:{v.get_name()}')

p1 = Person("ana", 86)
p2 = Person("james", 7)
c1 = Cat(1)
c1.set_name("furball")
c2 = Cat(1)
c2.set_name("fluffsphere")

d = {p1:c1, p2:c2}
make_pets(d)  # prints ana:furball
            #   james:fluffsphere

#########################################
################ AT HOME ################
#########################################
# Write the class Employee as a subclass of Person
class Employee(Person):
    ''' 
    An Employee contains an extra data attribute, salary as an int 
    '''
    def __init__(self, name, age):
        ''' 
        initializes self as a Person with a salary data attribute, initially 0.
        '''
        Person.__init__(self, name, age)
        self.salary = 0
        self.change = [0]
        
    def get_salary(self):
        ''' 
        returns self's salary.
        '''
        return self.salary
        
    def set_salary(self, s):
        ''' 
        - s is an int
        Sets self's salary data attribute to s.
        '''
        self.salary = s 
        self.change.append(s)
        
    def salary_change(self, n):
        ''' 
        - n is an int (positive or negative).
        Adds n to self's salary. If the result is negative, sets 
        self's salary to 0. Otherwise sets self's salary to the new value. 
        '''
        tot_salary = self.salary + n
        
        if tot_salary < 0:
            self.salary = 0
        
        else:
            self.salary = tot_salary
        
        self.change.append(self.salary)
        
    def has_friends(self):
        ''' 
        return True if self's friend list is empty and False otherwise.
        '''
        return bool(self.get_friends())
         
    def past_salaries_list(self):
        ''' 
        Keeps track of all salaries self has had in the order they've changed. 
        i.e. whenever the salary changes, keep track of it.
        Hint: you may need to add an additional data attribute to Employee.
        return a copy of the list of all salaries self has had, in order. 
        '''
        return self.change.copy()
    
    def past_salary_freq(self):
        ''' 
        return a dictionary where the key is a salary number and the 
        value is how many times self's salary has changed to that number. 
        '''
        d = {}
        
        # Loop: iterate over each number in list self.change
        for n in self.change:
            d[n] = d.get(n, 0) + 1
        
        return d
 
# # For example:
e = Employee("ana", 35)
print(e.get_salary())   # prints 0
e.set_salary(1000)
print(e.get_salary())   # prints 1000
e.salary_change(2000)
print(e.get_salary())   # prints 3000
e.salary_change(-50000)
print(e.get_salary())   # prints 0
print(e.has_friends())  # prints False
e.add_friend("bob")
print(e.has_friends())  # prints True
print(e.past_salaries_list())  # prints [0, 1000, 3000, 0]
print(e.past_salary_freq())  # prints {0: 2, 1000: 1, 3000: 1}

#########################################
# Write a function that meets this specification
def counts(L):
    ''' 
    - L: list, Employee and Person objects.
    ---
    #### return: 
        tuple of a count of:
            how many Person objects are in L.
            how many Employee objects are in L.
            the number of unique names among Employee and Person objects.
    '''
    count_per, count_emp = 0, 0
    unique_name = set(o.get_name() for o in L)
    
    # Loop: iterate over each element in L
    for e in L:
        if isinstance(e, Employee):
            count_emp += 1
        
        else:
            count_per += 1
    
    return (count_per, count_emp, len(unique_name))

# For example:
# make employees and people
L = []
L.append(Person('ana',8))
L.append(Person('bob',25))
L.append(Employee('ana',35))
L.append(Employee('cara',18))
L.append(Employee('dan',53))
# call function
print(counts(L))    # prints (2,3,4)