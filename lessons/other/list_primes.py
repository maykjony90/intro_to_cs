def is_prime(number):
    if (number <= 1) or (number != int(number)):
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def list_primes_to(last_num):
    list_primes = []
    # create a variable, list_primes, and set its value as an empty list
    for n in range(1, last_num + 1): # add 1 to include given number
        if is_prime(n):
            list_primes.append(n)
    return list_primes


def list_primes(number):
    primes_list = []
    for n in range(2, number + 1):
        if (number >= n):
            if (number % n == 0):
                primes_list.append(n)
                while number % n == 0:
                    number = number / n
        else: 
            return primes_list
    return primes_list

    

