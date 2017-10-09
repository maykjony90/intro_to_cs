# Write a procedure, shift, which takes as its input a lowercase letter,
# a-z and returns the next letter in the alphabet after it, with 'a' 
# following 'z'.

def shift(letter):
    # letter = letter.lower()
    let = ord(letter)
    if (let < ord('a')) or (let > ord('z')):
        return "Not a lowercase letter"
    let += 1
    if let == ord('z') + 1:
        return 'a'
    return chr(let)
    


print(shift('a'))
#>>> b
print(shift('n'))
#>>> o
print(shift('z'))
#>>> a
print(shift('A'))
