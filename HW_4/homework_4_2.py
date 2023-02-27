import random
import string


# Create the list dictionaries from 2 to 10.
def create_dicts():
    my_o = []  # Dicts list
    for _ in range(random.randint(2, 10)):  # Dictionary counter
        dictionary = {}
        for _ in range(random.randint(1, 26)):  # Elements counter
            # Key(random letter), value(random number from 0 to 100)
            dictionary[random.choice(string.ascii_lowercase)] = random.randint(0, 100)
        my_o.append(dictionary)  # Append every dictionary to the list
    return my_o


all_values = create_dicts()


def all_value_dict():
    my_o = {}
    c = 1
    for cntr in all_values:
        for key, value in cntr.items():
            if key not in my_o:  # Check whether value exists previously
                my_o[key] = {str(c): value}
            else:
                my_o[key][str(c)] = value
        c += 1
    return my_o


all_value_dict = all_value_dict()


def final_dict():
    my_dict = {}
    for key, value in all_value_dict.items():
        if len(all_value_dict[key]) == 1:
            my_dict[key] = max(all_value_dict[key].values())
        else:
            my_dict[key + "_" + str(max(all_value_dict[key], key=all_value_dict[key].get))] =\
                max(all_value_dict[key].values())
    return my_dict


for i in range(len(all_values)):
    print(f'Dict {i + 1}:  {all_values[i]}')  # Just for better displaying
print('')
print('Dictionary with all value for key:', dict(all_value_dict))
print('Final dictionary:', final_dict())
