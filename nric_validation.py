import re

def run():
    nric_number = input('Input NRIC Number : ')
    ic_st_alphabets = 'JZIHGFEDCBA'
    ic_fg_alphabets = 'XWUTRQPNMLK'

    first_letter = nric_number[0]
    digits = nric_number[1:-1]
    last_letter = nric_number[-1]

    if len(nric_number) != 9:
        print('Invalid NRIC length (must be exactly 9 characters, was given %d characters.)' % len(nric_number))
    if re.search('[^STFG]', first_letter):
        print('Invalid NRIC : %s (must be started with S, T, F, or G)' % first_letter)
    if re.search('[^0-9]', digits):
        print('Invalid NRIC Digits : %s (must be exactly in numbers)' % digits)

    sum_digits_value = 0
    for index,digit in enumerate(digits):
        if index == 0:
            multiplier = 2
            sum_digits_value += multiplier * int(digit)
            multiplier = 7
        else:
            sum_digits_value += multiplier * int(digit)
            multiplier -= 1

    if re.search('[TG]', first_letter):
        sum_digits_value += 4

    remainder = sum_digits_value % 11

    if re.search('[ST]', first_letter) and ic_st_alphabets[remainder] != last_letter:
        print('Invalid NRIC, last letter must be %s' % ic_st_alphabets[remainder])
    elif re.search('[FG]', first_letter) and ic_fg_alphabets[remainder] != last_letter:
        print('Invalid NRIC, last letter must be %s' % ic_fg_alphabets[remainder])
    else:
        print('NRIC is Valid')
        
    confirm_try = input('Try again (Y/N) ?')
    if re.search('[Yy]', confirm_try):
        print()
        run()
    else:
        print('Thank you for Demo')

run()