# Define a procedure, how_long_til_lunch, that takes
# three inputs: an integer representing the current hour,
# an integer representing the current minutes, and
# a string that is either 'am' or 'pm'.
#
# The output should be how long you have to wait from the
# given time until 11:45 am, in minutes (an integer).
#
# If you're unsure how the 12-hour clock works, see
# http://en.wikipedia.org/wiki/12-hour_clock
#
# For example, how_long_til_lunch(5, 45, 'pm') = 1080


def how_long_till_lunch(hour, minute, meridiem):
    '''(int, int, str) -> int
    Takes integers as hour and minute, and meridiem as string
    return how many minutes there are till lunch.

    >>> how_long_til_lunch(5, 45, 'pm')
    >>> 1080
    >>> how_long_til_lunch(5, 45, 'am')
    >>> 360
    '''
    # put a condition to avoid possible bugs.
    # Below condition is needed to be reformed!!!
    if (hour >= 12):
        print('Please enter a valid time integer')
    elif (minute >= 60):
        print('Please enter a valid time integer')
    elif (meridiem != 'am') and (meridiem != 'pm'):
        print('Enter either "am" or "pm"')
    else:
        # define variables that will be used in precedure
        min_in_hour=60
        twelve_hour_cycle = 12 * min_in_hour
        
        # Convert current time into minutes
        current_time = (hour*min_in_hour) + minute
        
        # Convert lunch into minutes by using items in lunch_time list.
        lunch_time_in_min = (lunch_time[0]*min_in_hour)+lunch_time[1]
        
        # Check if the meridiem in lunch time and in current time are equal
        # or not. If not, convert current time
        if meridiem != lunch_time[2]:
            current_time += twelve_hour_cycle
            
        # Check if current time is greater than lunch time. If so, assign a
        # new value for the current time. 
        if current_time > lunch_time_in_min:
            current_time -= twelve_hour_cycle*2
            
        # Subtract the current time from lunch time and return how many minutes
        # there are till lunch .
        how_long_in_min = lunch_time_in_min - current_time
        
        # Check if its lunch time. If so, wish 'bon appetite'!
        if how_long_in_min == 0:
            print('It\'s lunch time. \nEnjoy your meal!')
        return how_long_in_min
    
    
    

