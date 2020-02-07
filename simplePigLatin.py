import re
def pig_it(text):
    result = ''
    for x in re.split(r'\s', text):
        if re.match(r'\w+', x):
            print(x)
            result += x[1:] + x[0] +'ay '
        else:
            result += x 
    return result.strip()

pig_it('Pig latin is cool !') 