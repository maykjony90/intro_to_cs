

def shift(letter, n):
    letter_index = ord(letter) - ord('a')
    shifted_index = (letter_index + n) % 26
    return chr(ord('a') + shifted_index)


def rotate(s, n):
    return ''.join(c if c == ' ' else shift(c, n) for c in s)


print(rotate("naber guzelim", 3))
print(rotate('a', -27))
