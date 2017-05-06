def daysInMonths(year, month):
    ''' (int, int) -> int
    Takes two arguments as input and returns the corresponding
    days of the month accounting leap years.
    
    >>> daysInMonths(2012, 2)
    >>> 29
    >>> daysInMonths(2199, 1)
    >>> 31
    >>> daysInMonths(1900, 2)
    >>> 28
    '''
    if month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
        return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            return 28
        else:
            return 30
