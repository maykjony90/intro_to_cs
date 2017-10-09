def string_finder(any_text, any_value):
    counter = 1
    occurance_index = 0
    occurance_line = any_text.find(any_value, occurance_index)
    while occurance_line >= 0:
        output = (str(counter) + 'occurance of ' + any_value + ':'
        + str(occurance_line))
        print(output)
        counter+=1
        occurance_index = occurance_line + 1
        if occurance_line != int(occurance_line):
            print(occurance_line)

bozuk lan bu! whlie ogrenince tekrar yaz kodu ya da her ne gerekliyse
    
