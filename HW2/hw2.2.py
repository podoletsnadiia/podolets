# import modules
from collections import defaultdict
import random
import string

def dicts():
    my_o = []  # Dicts list
    for dict_num in range(random.randint(2, 10)):  # Dicts counter
        dictionary = {}
        for elem_num in range(random.randint(3, 7)):  # Elements counter
            dictionary[random.choice(string.ascii_lowercase)] = random.randint(0, 100)  # Key(ran_let), value(ran_num)
        my_o.append(dictionary)  # Append every dict to dicts list
    return my_o

output = {}  # To ensure you always get the
# correct output to include if there are negative
# values use float('-inf') as the default value
dicts = dicts()

c = 1
for cntr in dicts:  # Create a counter for later adding of '_number_of_dictionary' for the same keys
    for k, v in cntr.items():
        if k not in output:  # Check whether value exists previously
            output[k] = {str(c): v}
        else:
            output[k] [str(c)] = v
    c += 1

mylyn = {}
for k, v in output.items():
    if len(output[k]) == 1:
        mylyn[k] = max(output[k].values())
    else:
        mylyn[k + "_" + str(max(output[k], key=output[k].get))] = max(output[k].values())


for i in range(0, len(dicts)):
    print(f'Dict {i+1}:  {dicts[i]}')  # for better display
print('')
print('Key_dictionary:',(output))  # dictionary via key
print('Final dictionary:', (mylyn))

