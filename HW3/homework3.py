import re
a = """homEwork:
tHis iz your homeWork, copy these Text to variable.
You NEED TO normalize it fROM letter CASEs point oF View.also, create one MORE senTENCE witH LAST WoRDS of each existING 
SENtence and add it to the END OF this Paragraph.
it iZ misspeLLing here.fix“iZ” with correct “ is ”, but ONLY when it Iz a mistAKE.
last iz TO calculate nuMber OF Whitespace characteRS in this Text.caREFULL,
 not only Spaces, but ALL whitespaces.I got 87."""


my_o = ''
last_w = []

for i in a.lower().split('\n'):  # Convert into lower case and split it by '\n'
    for y in i.split('.'):  # Split again by '.'
        if y.find('iz') != -1:  # If 'iz' not False

            y = y.replace(' iz ', ' is ')  # Replace 'iz' into 'is'
        # Create lists with every word (but not number) of all sentences, including empty (when '/n')
        last_word = [i.replace(':', '') for i in y.split(' ') if i != '' and len(y) > 0 and not i.isdigit()]

        if len(last_word) > 0:  # If list not empty
            last_w.append(last_word[-1])  # Append last word from each sentence to list

        if y == '':  # Creating new punctuation marks
            my_o += '\n'  # Add new '\n'
        elif y[-1].isalpha():
            my_o += y.capitalize() + '. '  # Add new '. ' to the end of all sentences
        elif y[-1].isdigit():
            my_o += y.capitalize() + '.'  # For 'I got 87'
        elif y[-1] == ':':
            my_o += y.capitalize() + '\n'  # For 'Homework'

whitespaces = 0
for i in my_o:
    if i.isspace():
        whitespaces += 1

# print(my_o.count('\n') + my_o.count(' ')) another way of whitespaces count

last_w_sentance = ' '.join(last_w) + '.'  # Create a new sentence(string) from list 'last_w'
# The result
my_o = my_o[:my_o.find('paragraph.')+10] + '\n' + last_w_sentance.capitalize() + my_o[my_o.find('paragraph.')+10:]

print(my_o)
print('Count of all whitespaces:', whitespaces)
