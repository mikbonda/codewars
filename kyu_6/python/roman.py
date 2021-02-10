import sys
def solution(roman):
    # IV = 4
    # Check numbers to make sure the one afterwards isnt bigger for subtract notion
    skipped = False
    
    normal_num = 0

    print(roman)

    print("Length of string is : " + str(len(roman)))

    for element in range(0, len(roman)):
        if len(roman) == 1:
            return which_numeral(roman[element])
        if skipped:
            print("Skipping because manupuated value previously")
            skipped = False
            # break
        else:
            if element < len(roman)-1:
                if which_numeral(roman[element+1]) > which_numeral(roman[element]):
                    # This condition means that the previous element was smaller
                    # than the first one, resulting in subtraction
                    normal_num = normal_num + (which_numeral(roman[element + 1]) - which_numeral(roman[element]))
                    skipped = True
                else:
                    normal_num = normal_num + which_numeral(roman[element])
            else:
                normal_num = normal_num + which_numeral(roman[element])
    
    return normal_num


def which_numeral(roman_numeral):
    if roman_numeral == 'I':
        return 1
    elif roman_numeral == 'V':
        return 5
    elif roman_numeral == 'X':
        return 10
    elif roman_numeral == 'L':
        return 50
    elif roman_numeral == 'C':
        return 100
    elif roman_numeral == 'D':
        return 500
    elif roman_numeral == 'M':
        return 1000
    else:
        return 'INVALID NUMVER'

print(solution(sys.argv[1]))