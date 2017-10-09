def dateIsBefore(year1, month1, day1, year2, month2, day2):
    ''' (int, int ,int, int, int, int) -> Boolean
    Returns True if year1-month1-day1 is before
    year2-month2-day2. Otherwise, returns False.
    
    >>> dateIsBefore(2012, 1, 3, 2012, 2, 4)
    >>> True
    >>> dateIsBefore(2012, 11, 30, 2013, 5, 8)
    >>> True
    >>> dateIsBefore(2012, 2, 4, 2012, 2, 4)
    >>> False
    '''
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False
            
print dateIsBefore(2012, 1, 3, 2012, 2, 4)
print dateIsBefore(2012, 11, 30, 2013, 5, 8)
print dateIsBefore(2012, 2, 4, 2012, 2, 4)
