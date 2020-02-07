import nltk
nltk.corpus.gutenberg.fileids()

#Gutenberg Corpus

#emma = nltk.Text(nltk.corpus.gutenberg.words('austen-emma.txt'))
#len(emma)
#emma.concordance("surprize")
from nltk.corpus import gutenberg
gutenberg.fileids()
emma = gutenberg.words("austen-emma.txt")

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
    print(int(num_chars/num_words), int(num_words/num_sents), int(num_words/num_vocab), fileid)

# Web and Chat Text

from nltk.corpus import webtext
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:65], '...')

from nltk.corpus import nps_chat
chatroom = nps_chat.posts('10-19-20s_706posts.xml')
chatroom[655]

# Brown Corpus

from nltk.corpus import brown
brown.categories()
brown.words(categories='belles_lettres')
brown.words(fileids=['cg22'])
brown.sents(categories=['news', 'editorial', 'reviews'])

news_text = brown.words(categories='news')
fdist = nltk.FreqDist([w.lower() for w in news_text])
modals = ['can', 'could', 'may', 'might', 'must', 'will']
for m in modals:
    print(m + ':', fdist[m])

cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre))

genres = ['news', 'religion', 'hobbies', 'science_fiction', 'romance', 'humor']
modals = ['can', 'could', 'may', 'might', 'must', 'will']
cfd.tabulate(conditions=genres, samples=modals)

# Reuters Corpus

from nltk.corpus import reuters
reuters.fileids()
reuters.categories()

# inaugural address corpus

from nltk.corpus import inaugural
inaugural.fileids()
[fileid[:4] for fileid in inaugural.fileids()]

cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target))
cfd.plot()

# corpora in other langs

from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang+'-Latin1')
)
cfd.plot(cumulative=True)

# Counting Words by genre

from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre, word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)

genre_word = [
    (genre, word) 
    for genre in ['news', 'romance']
    for word in brown.words(categories=genre)
]
len(genre_word)

genre_word[130444:130450]

cfd = nltk.ConditionalFreqDist(genre_word)
cfd.conditions()
list(cfd['romance'])
cfd['romance']['love']

# Plotting and Tabulating Distributions

from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
    (target, fileid[:4])
    for fileid in inaugural.fileids()
    for w in inaugural.words(fileid)
    for target in ['america', 'citizen']
    if w.lower().startswith(target)
)

from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch','Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
    (lang, len(word))
    for lang in languages
    for word in udhr.words(lang + '-Latin1')
)
cfd.tabulate(conditions=['English', 'German_Deutsch'],
    samples=range(10), cumulative=True)
