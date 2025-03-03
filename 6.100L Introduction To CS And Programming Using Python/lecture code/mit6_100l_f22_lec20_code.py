#########################################
########### YOU TRY IT ##################
#########################################
# Create one Workout object saved as variable w_one, 
# from Jan 1 2021 at 3:30 PM until 4 PM. 
# You want to estimate the calories from this workout. 
# Print the number of calories for w_one.
w_one = Workout('Jan 1 2021 at 3:30 PM', 'Jan 1 2021 at 4:00 PM')
print(w_one.get_calories())

# Create another Workout object saved as w_two, 
# from Jan 1 2021 at 3:35 PM until 4 PM. 
# You know you burned 300 calories for this workout.  
# Print the number of calories for w_two. 
w_one = Workout('Jan 1 2021 at 3:35 PM', 'Jan 1 2021 at 4:00 PM', 300)
w_one.set_calories(300)
print(w_one.get_calories())

#########################################
################ AT HOME ################
#########################################
def total_elapsed_time(L):
    '''
    - L: list of tuples, (e1, e2) where:
        - e1 and e2 are strings representing a date and time. e.g. '9/30/2021 1:35 PM'.
        - e2 occurs later in time than e1.
    ---
    #### return:
        sum of all the elapsed times, in seconds, in L. 
    ---
    #### Note:
        Consider the elapsed time for a tuple to be the difference between e2 and e1.
    '''
    tot = 0
    
    # Loop: iterate over each tuple in list L
    for e in L:
        e1 = parser.parse(e[0])
        e2 = parser.parse(e[1])
        tot += (e2 - e1).total_seconds()
    
    return tot
    
t1 = '1/1/2021 2:00 PM'
t2 = '1/1/2021 2:05 PM'
t3 = '3/12/2021 1:22 PM'
t4 = '3/12/2021 1:32 PM'
t5 = '7/13/2021 6:00 PM'
t6 = '7/13/2021 6:02 PM'
L = [(t1, t2), (t3, t4), (t5, t6)]  # 5min + 10min + 2min = 1020 sec
print(total_elapsed_time(L))    # prints 1020