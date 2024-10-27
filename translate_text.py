from translate import Translator

translator = Translator(to_lang="french") 

text = "Hello, what's your name?"

translation = translator.translate(text)

print(translation)