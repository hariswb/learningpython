def highest(s):
    words = s.split()
    scores = [sum([ord(l)-96 for l in w]) for w in words]
    dict_scores = dict(zip(words,scores))
    print(dict_scores)
    print(max(dict_scores, key=dict_scores.get))

highest('wyhyjxfey qusbtmymil')
###someone coded it this way
###  return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))