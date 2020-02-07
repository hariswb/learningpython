def checkPalTwo(number):
    i = 1
    num = number
    otherNum = 0
    while num > 0:
        x = round((num/10 - num//10)*10)
        y = x/10**(i-1)
        otherNum += y
        num //= 10
        i += 1 
    #print(round(otherNum*10**(i-2)), number)
    if number - otherNum == 0:
        return True
    else: 
        return False

checkPal(1899991)