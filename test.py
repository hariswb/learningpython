def friend(x):
    result = []
    for name in x:
        if len(name) == 4:
            #print("friend")
            result.append(name)
#        else:
            #print("fwoe")
    return result 
    
print(friend(["Ryan", "Kieran", "Mark"]))

def friendComprehension(x):
        return [i for i in x if len(i)==4]
        

print(friendComprehension(["Ryan", "Kieran", "Mark"]))