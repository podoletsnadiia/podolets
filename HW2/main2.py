# def function(n):
#     pick = randrange(n)
#     return {'key %d' % i: ('value1', 'value2')[i == pick] for i in range(n)}




from random import randint, choice # using the `random` module’s `.choices()` method
from string import ascii_lowercase
#
final_dict, indexes_dict = {}, {}

# rand_list = [{choice(ascii_lowercase): randint(0, 100) for i in range(len(ascii_lowercase))} for j in range(randint(2, 10))]
#
# for dictionary in rand_list:
#     for key, value in dictionary.items():
#         if key not in final_dict:
#             final_dict.update({key: value}) # add first occurrence
#         else:
#             if value < final_dict.get(key):
#                 #TODO indexes_dict.update({:})
#                 continue
#             else:
#                 final_dict.update({key: value})
#                 #TODO indexes_dict.update({:})
#
# for key in indexes_dict:
#     final_dict[key + '_' + str(indexes_dict[key])] = final_dict.pop(key)

print(final_dict)