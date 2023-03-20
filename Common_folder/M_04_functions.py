a = """
homEwork:
tHis iz your homeWork, copy these Text to variable.

You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.
it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.
last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87.
"""


def normalization():
    my_o = ''
    for i in a.lower().split('\n'):  # Convert string into lower case and split it by '\n'
        for y in i.split('.'):  # Split again by '.'
            if y.find('iz') != -1:  # If 'iz' not False

                y = y.replace(' iz ', ' is ')  # Replace 'iz' with 'is' add space for replacement only where it's needed

            # Creating new punctuation marks
            if y == '':
                my_o += '\n'  # Add new '\n'
            elif y[-1].isalpha():
                my_o += y.capitalize() + '.'  # Add new '. ' to the end of every sentence
            elif y[-1].isdigit():
                my_o += y.capitalize() + '.'  # For sentence 'I got 87'
            elif y[-1] == ':':
                my_o += y.capitalize() + '\n'  # For sentence 'Homework'
    return my_o


normalized_text = normalization()


def creation_of_last_words_sentence():
    last_words_sentence = ''
    last_words = []
    for i in a.lower().split('\n'):  # Convert string into lower case and split it by '\n'
        for y in i.split('.'):  # Split again by '.'
            last_word = [i.replace(':', '') for i in y.split(' ') if i != '' and len(
                y) > 0]  # Create lists with every word of every sentence, including empty (when '/n')

            if len(last_word) > 0:  # If list not empty
                last_words.append(last_word[-1])  # Append last word from each sentence to list

        last_words_sentence: str = ' '.join(last_words) + '.'  # Create a new sentence(string) from list 'last_words'
    return last_words_sentence


last_words_sentence = creation_of_last_words_sentence()

# Count of numbers of whitespaces


def whitespace_count():
    whitespaces = normalized_text.count('\n') + normalized_text.count(' ')
    return whitespaces


# Add new sentence to the end of paragraph
def append_new_sentence():
    result = normalized_text[:normalized_text.find('paragraph.')+10] \
             + '\n' + last_words_sentence.capitalize() + normalized_text[normalized_text.find('paragraph.')+10:]
    return result


print(append_new_sentence())
print('Count of whitespaces:', whitespace_count())
