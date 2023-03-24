import sys

# import all modules from previous tasks
import M_04_functions
from M_04_functions import normalization
import M_05_Classes
import M_06_Files
import M_07_csv
from M_07_csv import create_csv1, create_csv2
import M_08_JSON
import M_09_XML
import M_10_db

# new_publication_object = Publication(input('Choose what you want to publish (News, Private Ad, Useful Tips): ').upper().strip(), input('Text: '))
# new_publication_object.publishing()

news = M_05_Classes.News()

while True:
    print('Choose what you want to publish:\n1 - News\n2 - Private Ad\n3 - Useful Tips\n\n0 - Exit\n')
    a = input('Select number: ')
    if a == '1':
        news.publishing()
        # csv.recalculate()
        create_csv1()
        create_csv2()
        print("Call class News")
    elif a == '2':
        print("Call class Private Ad")
    elif a == '3':
        print("Call class Useful Tips")
    elif a == '0':
        exit()