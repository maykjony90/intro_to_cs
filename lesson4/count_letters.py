def count_letters(line):
    ''' <string> -> <number>
    Takes a string, line, as input and returns the numbers of the alphanumeric
    characters in given input excepting whitespaces.
    '''
    for n in char:
        if n.isspace():
            continue
        else:
            score += score.join(n)

    return len(score)
