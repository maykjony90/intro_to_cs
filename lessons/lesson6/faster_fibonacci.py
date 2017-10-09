# Define a faster fibonacci procedure that will enable us to computer
# fibonacci(36).ArithmeticError


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    i = 1
    fib_pre_2 = 0
    fib_pre_1 = 1
    while i < n:
        result = fib_pre_2 + fib_pre_1
        fib_pre_2 = fib_pre_1
        fib_pre_1 = result
        i += 1
    return result


def faster_fibonacci(n):  # Udacity's solution, It's fucking udacious!!!
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current


print(fibonacci(5))
print(faster_fibonacci(5))
# print(fibonacci(36))
# >>> 14930352
