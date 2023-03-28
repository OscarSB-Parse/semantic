# Both codes work in the same way
# Create 3 variables to store 3 strings and apply NLP and procede to print their similarity
# Use a for loop to print iterate through the variable called tokens and see the resultd display in a friendly way 
# word to compare 1, word to compare 2, similarity between the words
# The principal difference between the models used to run the code is based in the accuracy of the predictions
# gorilla-monkey 0.3722374141216278  using (en_core_web_sm) model 
# gorilla-monkey 0.9999998807907104  using (en_core_web_md) model
"""
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word2))

tokens = nlp ("cat apple monkey banana")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text , token2.text,token1.similarity(token2))

"""
import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("man")
word2 = nlp("woman")
word3 = nlp("gorilla")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word2))

tokens = nlp ("man woman monkey gorilla")

for token1 in tokens:
    for token2 in tokens:
        print(f"{token1.text} -  {token2.text} : similarity: {token1.similarity(token2)}")

