'''Second'''
if __name__ == '__main__':
    with open('stdin.txt', encoding = 'utf-8') as filein:
        content = filein.read()
        FIRST = content[1]
        SECOND = content[2]
        THIRD = content[3]
        SUM = FIRST + SECOND + THIRD
        MULT = FIRST * SECOND * THIRD
        HOME_FIRST = (1/FIRST)
        HOME_SECOND = (1/SECOND)
        HOME_THIRD = (1/THIRD)
    with open('stdout.txt', 'x', encoding = 'utf-8') as fileout:
        fileout.write(SUM, MULT, HOME_FIRST, HOME_SECOND, HOME_THIRD)
        
