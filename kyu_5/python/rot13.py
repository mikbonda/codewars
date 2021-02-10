import sys

def rot13(message):

    if len(message) == 0:
        return ''
    hex_array = tohex(message)
    which_case_array = which_case(message)

    rot13_array = rot13_shift(hex_array)

    rot13_str = tochar(rot13_array)

    converted_string = change_case(rot13_str, which_case_array)

    print("Before value: " + message)

    print("After value: " + converted_string)
    
    return converted_string

    pass

def which_case(message):
    case_array = []
    for element in range(0, len(message)):
        if message[element].isupper():
            case_array.append('u')
        elif message[element].islower():
            case_array.append('l')
        else:
            case_array.append('l')
    return case_array


def tohex(message_string):
    h_array = []

    for element in range(0, len(message_string)):
        h_array.append(ord(message_string[element].lower()))

    return h_array

def rot13_shift(h_array):
    # upper case A is 65
    # lower case z is 122
    new_array = []
    rot_shift_value = 13
    for element in h_array:
        # If is a non standard A-Za-z char, keep the value
        if element < 65 or element > 122:
            new_array.append(element)
        elif (element + 13) % 123 < 65:
            new_array.append(((element + 13) % 123)+65)
        else:
            new_array.append((element + 13) % 123)
    
    return new_array

def tochar(rot_h_array):
    new_rot_char = [] 
    for element in rot_h_array:
        new_rot_char.append(chr(element))
    
    return new_rot_char

def change_case(char_array, case_array):
    case_changed_array = []
    for element in range(0, len(char_array)):
        if 'l' in case_array[element]:
            case_changed_array.append((char_array[element].lower()))
        elif 'u' in case_array[element]:
            case_changed_array.append((char_array[element].upper()))
    
    return ''.join(case_changed_array)



rot13(sys.argv[1])