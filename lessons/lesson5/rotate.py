# Write a procedure, rotate which takes as its input a string of lower case
# letters, a-z, and spaces, and an integer n, and returns the string constructed
# by shifting each of the letters n steps, and leaving the spaces unchanged.
# Note that 'a' follows 'z'. You can use an additional procedure if you
# choose to as long as rotate returns the correct string.
# Note that n can be positive, negative or zero.


def rotate(lowercase_string, n):
    # Your code here
    decoded_string = ""
    for char in lowercase_string:
        if char != " ":
            decoded_char = shift_n_letters(char, n)
            decoded_string += decoded_char
        elif char == " ":
            decoded_string += char
        else:
            decoded_string += decoded_char
    return(decoded_string)


def shift_n_letters(letter, n):
    a = ord('a')
    z = ord('z')
    let = ord(letter)
    total_n_letters = 26
    if (let < a) or (let > z):
        print("please enter a lowercase letter")
    else:
        if n < 0:
            n = abs(n) % total_n_letters
            let = let - n
            # let = let - ((n * -1) % total_n_letters)
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


print(rotate('sarah', 13))
# >>> 'fnenu'
print(rotate('fnenu', 13))
# >>> 'sarah'
print(rotate('dave', 5))
# >>>'ifaj'
print(rotate('ifaj', -5))
# >>>'dave'
print(rotate(("zw pfli tfuv nfibj tfiivtkcp pfl jyflcu "
              "sv rscv kf ivru kyzj"), -17))
# >>> ???
