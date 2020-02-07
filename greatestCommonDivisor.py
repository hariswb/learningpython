def gcd(a,b):
    arr1 = [x for x in range(1,a) if a % x == 0]
    arr2 = [x for x in range(1,b) if b % x == 0]
    #print(arr1, arr2)
    return [x for x in arr1 if x in arr2][-1]
