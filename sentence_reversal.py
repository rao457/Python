
def sentence_reverse(sentence):  
    sentence = sentence.split()
    sentence.reverse()
    sentence = ' '.join(sentence)
    return sentence
sentence = 'The dark brown fox jumped over the lazy dog'
print(sentence_reverse(sentence))