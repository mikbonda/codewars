import sys

def solution(s):
    split_str_array = []
    for element in range(0, len(s)):
        if element == 0:
            split_str_array.append(s[element])
        else:
            if s[element].isupper():
                split_str_array.append(' ')
            split_str_array.append(s[element])
    
    return ''.join(split_str_array)

print(solution(sys.argv[1]))