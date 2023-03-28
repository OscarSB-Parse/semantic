"""import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
print("lol")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word2))

tokens = nlp ("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text , token2.text,token1.similarity(token2))"""


import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("house")
word2 = nlp("church")
word3 = nlp("avenue")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word2))

tokens = nlp ("man woman church avenue")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text , token2.text,token1.similarity(token2))