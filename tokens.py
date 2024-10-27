import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk import ngrams


s = 'this is me and I am going to be the best in the world'

tokens = word_tokenize(s)

print(f'Tokens:{tokens}')

# Unigrams
unigrams = list(ngrams(tokens,1))
print(f'Unigrams: {unigrams}')

# Bigrams
bigrams = list(ngrams(tokens,2))
print(f'Bigrams: {bigrams}')

# Trigrams
trigrams = list(ngrams(tokens,3))
print(f'Trigrams: {trigrams}')

 


