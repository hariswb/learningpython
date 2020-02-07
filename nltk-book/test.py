import nltk
from nltk.book import *

def lexical_diversity(text):
    return len(set(text)) / len(text)

text2.dispersion_plot(['Elinor', 'Marianne', 'Edward', 'Willoughby'])

list(text5.collocation_list())

phrase1 = text1[123:137]
phrase2 = text1[442:454]

len(phrase1 + phrase2) 
len(phrase1)+ len(phrase2)

[index(w) for w in sent3 if 'the' in w]