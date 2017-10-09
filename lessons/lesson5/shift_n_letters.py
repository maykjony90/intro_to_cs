# procedure, shift_n_letters which takes as its input a lowercase
# letter, a-z, and an integer n, and returns the letter n steps in the
# alphabet after it. Note that 'a' f ollows 'z', and that n can be positive,
# negative or zero.


def shift_n_letters(letter, n):
    a = ord('a')
    z = ord('z')
    let = ord(letter)
    total_n_letters = 26  # number of letters in the alphabet in ASCII.
    if (let < a) or (let > z):
        print("please enter a lowercase letter")
    else:
        if n < 0:
            n = abs(n) % total_n_letters
            let = let - n
            if let < a:
                let = (z + 1) - (a - let)  # z minus 1:from where to start count
                return(chr(let))
            return(chr(let))
        elif n > 0:
            n = n % total_n_letters
            let = let + n
            if let > z:
                let = (a - 1) + (let - z)  # a minus 1: from where to count
                return(chr(let))
            return(chr(let))
        else:
            return(chr(let))


print(shift_n_letters('s', 1))
# >>> t
print(shift_n_letters('s', 2))
# >>> u
print(shift_n_letters('s', 10))
# >>> c
print(shift_n_letters('s', -10))
# >>> i
print(shift_n_letters('s', -20))
# >>> y
print(shift_n_letters('a', -1))
# >>> z
print(shift_n_letters('z', 1))
# >>> a
print(shift_n_letters('t', 0))
# >>> t
