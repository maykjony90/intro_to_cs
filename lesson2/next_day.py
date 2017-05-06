# simple precedure that takes three arguments year, month and day
# and return the next day as year month and day.
# This version incorrectly assumes all month have 30 days!!!


def nextDay(year, month, day):
    ''' (int, int, int) -> (int, int, int)
    Warning: this version incorrectly assumes all months have 30 days!
    Takes three int as input year-month-day and returns
    next day's date as year-month-day
    
    >>> nextDay(2012, 11, 3)
    >>> (2012, 11, 4)
    >>> nextDay(2012, 11, 30)
    >>> (2012, 12, 1)
    >>> nextDay(2012, 12, 30)
    >>> (2013, 1, 1)
    '''
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

print nextDay(2012, 11, 3)
#(2012, 11, 4)
print nextDay(2012, 11, 30)
#(2012, 12, 1)
print nextDay(2012, 12, 30)
#(2013, 1, 1)
