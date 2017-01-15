s = 'abcdeeeeegabcdefghijk'
string = ''
pos = 0
tempstring = ''
longstring = ''


for l in s:
    if string == '':
        string = l
    else:
        if l >= string[-1]:
            string += l
            if len(s) == pos + 1:
                tempstring = string
        else:
            tempstring = string
            string = l
    if len(tempstring) > len(longstring):
        longstring = tempstring

    pos += 1

print('Longest substring in alphabetical order is: ' + str(longstring))