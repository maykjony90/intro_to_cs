# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number first_element in the string is less than or equal 
# to the preceding number second_element, the number first_element should be inserted 
# into a sublist. Continue adding the following numbers to the 
# sublist until reaching a number z that
# is greater than the number second_element. 
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number

### A further challange: ###
# Define a precedure without adding first item into result_list list beforehand!!!

def numbers_in_lists(string):
    input_list = [] 
    for num in list(string): # convert each item into integer and append them
        input_list.append(int(num))
    result_list = [input_list[0]] # add the first item into result_list beforehand
    sub_list = [] # temporary list to collect items
    second_element = 0 # first element to be compared
    first_element = 1 # second element to be compared
    if len(input_list) > 1: # input list must contain more than 1 element
        while first_element < len(input_list):
            if input_list[first_element] > input_list[second_element]:
                result_list.append(input_list[first_element])
                second_element += 1
                first_element += 1
            else:
                # first condition is to be check is if first_element is less
                # than length of input_list. So put it as a first condition.
                # If you put it at second, it will throw an error as the
                # value of first_element will be out of index.
                while (first_element < len(input_list)) and \
                      (input_list[second_element] >= input_list[first_element]):
                    # hold value of index second_element
                    # be compared.
                    sub_list.append(input_list[first_element])
                    # keep adding value of first_element into the
                    # into a sublist till finding a
                    # value that is greater than first_element.
                    first_element += 1                     
                result_list.append(sub_list)            
                sub_list = [] # when a greater value found, empty sub_list
                second_element = first_element - 1
        return result_list
    else:
        return False    

'''
#testcases
string = '543987'
result = [5,[4,3],9,[8,7]]
print repr(string), numbers_in_lists(string) == result
string= '987654321'
result = [9,[8,7,6,5,4,3,2,1]]
print repr(string), numbers_in_lists(string) == result
string = '455532123266'
result = [4, 5, [5, 5, 3, 2, 1, 2, 3, 2], 6, [6]]
print repr(string), numbers_in_lists(string) == result
string = '123456789'
result = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print repr(string), numbers_in_lists(string) == result
'''
