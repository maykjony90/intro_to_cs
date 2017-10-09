def test():

    assert deep_count([1, 2, 3]) == 3
    assert deep_count([]) == 0
    assert deep_count([1, 3, [4, [], [5, 6]]]) == 8, "base case'i bulamiyorum"

    print("All tests pass.")
    return


def is_list(p):
    return isinstance(p, list)


def deep_count_myVer(p):
    if len(p) == 0:
        return 0
    else:
        for item in p:
            if is_list(item):
                if item != []:
                    return len(p) + deep_count(item)
        return len(p)


# Udacity's Solution:
def deep_count(p):
    sum = 0
    for e in p:
        sum = sum + 1
        if is_list(e):
            sum = sum + deep_count(e)
    return sum


print(test())
