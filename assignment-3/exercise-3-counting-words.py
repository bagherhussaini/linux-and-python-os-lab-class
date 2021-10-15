sentence = input('Enter a Sentence to Count Its Words: ').strip()
word_counter = 1
for char in sentence:
    if char == ' ':
        word_counter += 1
print('Number of Words: ', word_counter)
