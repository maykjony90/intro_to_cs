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
    if day < daysInMonths(year, month):
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

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

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ''' (int, int, int, int, int, int) -> int
    Takes six arguments as input and returns total days past from
    year1-month1-day1 till year2-month2-day2. Accounting leap years.
    
    >>> daysBetweenDays(2012,1,1,2012,2,28)
    >>> 58
    >>> daysBetweenDays(2012,1,1,2012,3,1)
    >>> 60
    >>> daysBetweenDays(2011,6,30,2012,6,30)
    >>> 366
    '''
    days = 0
    while nextDay(year1, month1, day1) != (year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
    
def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
