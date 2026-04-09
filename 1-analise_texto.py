import os
import nltk
from nltk import sent_tokenize, word_tokenize

# nltk.download('punkt')
# nltk.download('punkt_tab')

# 1 - Importação do Texto
with open(os.path.join('data', 'texto.txt'), 'r', encoding='utf-8') as file :
    texto = file.read()
    print(texto)
    
# 2 - Tokenizando o Texto
sent_tokens = sent_tokenize(texto)
print(sent_tokenize)
print(len(sent_tokens))

word_tokens = word_tokenize(texto)
print(word_tokens)
print(len(word_tokens))