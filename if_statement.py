sentence = 'Hello World'
excited = True
if excited:
    sentence_copy = sentence  ### we can avoid disturbing original variable value by shaalow copying it to another variable
    sentence_copy += '!'
print(sentence)
print(sentence_copy)