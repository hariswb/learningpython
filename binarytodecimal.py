##Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

def binToDec(bin):
    bit = 0
    int = 0
    for i in range(4):
        bit=bin[len(bin)-1-i]
        if  bit == 1:
            int+=2**i
    return int


binToDec([1, 0, 1, 1])