def isLeapYear(year):
    ''' (int) -> Boolean
    Returns True if year is a leap year. Otherwise,
    returns False.
    
    >>> isLeapYear(2100)
    >>> False
    >>> isLeapYear(2012)
    >>> True
    >>> isLeapYear(1900)
    >>> False
    '''
    if (year % 4 is 0) and (year % 100 is not 0) or (year % 400 is 0):
        return True
    else:
        return False

''' An alternative way '''

"""

def isLeapYear(year):
    ''' (int) -> Boolean
    Returns True if year is a leap year. Otherwise,
    returns False.
    
    >>> isLeapYear(2100)
    >>> False
    >>> isLeapYear(2012)
    >>> True
    >>> isLeapYear(1900)
    >>> False
    '''
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

print isLeapYear(2012)
print isLeapYear(2013)
print isLeapYear(2014)
print isLeapYear(1900)
print isLeapYear(3)

"""
