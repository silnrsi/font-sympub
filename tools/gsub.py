#!/usr/bin/python3

glyphs_names = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

for tens in range(10):
    for ones in range(10):
        # convert to text
        tens_name = glyphs_names[tens]
        ones_name = glyphs_names[ones]

        # special handling for single digits
        glyphs = f'{tens_name} {ones_name}'
        number = f'{tens}{ones}'
        if tens == 0:
            glyphs = ones_name
            number = ones

        # output GSUB
        print(f'    sub {glyphs} circlenum by circlednum{number};')
