def to_camel_case(text):
    new_text_array = []

    if len(text) == 0:
        return ''
        
    for element in range(0, len(text)):
        if text[element].isalpha():
            if element > 0 and (text[element-1] == '-' or text[element-1] ==  '_'):
                new_text_array.append(text[element].upper())
            else:
                new_text_array.append(text[element])
            
    
    return ''.join(new_text_array)