def namelist(names):
    y = [x['name'] for x in names]
    if len(y) >= 3:
        return ', '.join(y[:-1])+' & '+y[-1]
    elif len(y) == 2:
        return ' & '.join(y)
    elif len(y) == 1:
        return y[0]
    else:
        return '' 

namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])