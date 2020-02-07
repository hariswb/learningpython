def persistence(n):
    result=n
    step=0
    while result//10 > 0:
        #print(result//10)
        count = 0
        digMultiple=1
        while result//(10**count) > 0:
            dig=result//(10**count)%10
            count += 1
            digMultiple*= dig
        result=digMultiple
        #print(result)
        step+=1
    return step

print(persistence(999))