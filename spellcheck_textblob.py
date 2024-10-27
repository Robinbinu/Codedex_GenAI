from textblob import TextBlob

text = 'I loe pogamming anfd cats'

blob = TextBlob(text)

print(blob.correct())