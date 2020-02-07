def find_missing(x):
    d = (x[len(x)-1]-x[0])/(len(x))
    print(d)
    i = 1
    while x[i-1] == x[0]+(i-1)*d:
        print(i, x[i-1], x[0]+(i-1)*d)
        i += 1
    
    return x[0]+(i-1)*d

find_missing([1, 3, 5, 7, 9, 13])