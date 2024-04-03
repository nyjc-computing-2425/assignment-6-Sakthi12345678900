from datetime import datetime, timedelta
import time

    # Part 1
def clock(n):
    # Your code here
        '''
        Show time and update every second for n number of seconds in HH:MM:SS
        '''
        t_with_mm = datetime.now()
        stop_time = t_with_mm + timedelta(seconds = n)
        while t_with_mm < stop_time:
            t_without_mm = t_with_mm.strftime('%H:%M:%S')
            print(t_without_mm, end = '\r') 
            time.sleep(1) 
            t_with_mm = datetime.now()



# Part 2
def lcm(a, b):
    # Your code here
    ''' 
    Calculates the lowest common multiple of a and b
    '''
    a_original = a
    b_original = b
    while a != b:
        if a < b:
            a += a_original
        else:
            b += b_original

    return a 





# Part 3
def gcf(a, b):
    # Your code here
    ''' 
    Calculate the highest commom factor of a and b
    '''
    while b != 0:
        r = a % b
        a = b
        b = r
    return a
