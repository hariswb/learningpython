def countBits(n):
    r = 0
    count = 0
    while n > 0:
        r, n = n % 2, n // 2
        count+=r 
        print(n,r, count)
    return count
    
countBits(13)
