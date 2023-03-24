from datetime import datetime
import os
import pathlib
import M_04_functions as Imported_file
import re

PATH = os.path.join(pathlib.Path.cwd(), 'newsfeed.txt')
print(PATH)

text_str = """
<NEWS> 
<TEXT> First News
with
additional
strings!
</TEXT>
<CITY>London</CITY>
</NEWS>

<PRIVATE AD>
<TEXT>sdfsdf</TEXT>
<DATE>23/03/2023</DATE>
</PRIVATE AD>

<NEWS> 
<TEXT> Second News
with
additional
strings!
</TEXT>
<CITY>London</CITY>
</NEWS>

<USEFUL TIPS>
<TEXT>sdfsdf</TEXT>
<AUTHOR>nadia</AUTHOR>
</USEFUL TIPS>

"""

# (?:<NEWS>) - начало блока
# (.*?) - тело блока до конца блока
# (?:</NEWS>) - конец блока
# re.DOTALL - параметр позволяет работать с многострочными данными

News = re.findall(r"(?:<NEWS>)(.*?)(?:</NEWS>)", text_str, re.DOTALL)  # for news
PrivateAd = re.findall(
    r"(?:<PRIVATE AD>)(.*?)(?:</PRIVATE AD>)", text_str, re.DOTALL
)  # for AD
UsefulTips = re.findall(r"(?:<USEFUL TIPS>)(.*?)(?:</USEFUL TIPS>)", text_str, re.DOTALL
)  # for useful tips

print(News)
print(PrivateAd)
print(UsefulTips)

print(*News, sep="\n")  # так можно напечатать список раскрытым
print(*PrivateAd, sep="\n")
print(*UsefulTips, sep="\n")


# Create parent class with parameters and methods which will be used in every child class
# The 'body' parameter will be overwritten several times and in the final form
# will be equal to the value of the entire publication that will be written to the file
class Publication:
    def __init__(self, data_type, text_str, body=''):
        self.data_type = data_type
        self.text = text_str
        self.body = body

    # Function that add body of publication to file
    def write_to_file(self):
        print(f'\nINFO. NewPublicationObject:\n{self.body}')
        try:
            # encoding="utf-8" for file
            with open(PATH, 'a', encoding="utf-8") as f:
                f.write(self.body)
            print('INFO. Successful. New publication added.')
            return True
        except Exception as e:
            print(f'ERROR. Fail. New publication was not added. Error: {e}')
            return False

    # Function that will create a new 'body'(entire publication) for every data_type of publication
    def publishing(self):
        def p1():
            return News(data_type=self.data_type, text=self.text_str, body=self.body, city=input('City: ')).body

        def p2():
            return PrivateAd(data_type=self.data_type, text=self.text_str, body=self.body).body

        def p3():
            return UsefulTips(data_type=self.data_type, text=self.text_str, body=self.body, author=input('Author: ')).body

        try:
            # Create a dict where keys are data_types of publications, values are functions created above
            self.body = {"NEWS": p1, "PRIVATE AD": p2, "USEFUL TIPS": p3}[self.data_type]()
        except Exception as e:
            print(f'\nERROR. Incorrect publishing data_type. Available data_types '
                  f'(News, Private Ad, Useful Tips). Error: {e}')
            return False

        # Call other method-function of the class from here
        return True if Publication.write_to_file(self) else False


# Child class News with new parameters
class News(Publication):
    def __init__(self, text_str, data_type, city, body, date_time=datetime.now().strftime("%d/%m/%Y, %H:%M")):
        # The super() function is used to give access to methods and properties of a parent class.
        super().__init__(data_type, text_str, body)
        self.city = city
        self.date_time = date_time
        self.body = f'News -------------------------\n{self.text_str}\n{self.city.casefold().capitalize().strip()},' \
                    f' {self.date_time}\n------------------------------'


# Child class PrivateAd with new parameters
class PrivateAd(Publication):
    def __init__(self, data_type, text_str, body):
        super().__init__(data_type, text_str, body)
        self.date_delta = PrivateAd.delta_time()
        self.body = f'Private Ad -------------------\n{self.text_str}\nActual until: ' \
                    f'{self.date_delta} days\n------------------------------'

    @staticmethod
    def delta_time():
        str_d1 = input('Please input "Actual until" date in format d/m/Y: ')

        try:
            # Convert string data data_type to datetime data_type for inputted date
            d1 = datetime.strptime(str_d1, "%d/%m/%Y")
        except Exception as e:
            print(f'ERROR. Enter date in followed format next time: d/m/Y. Error: {e}')
            return False

        # Double conversion for publishing date (datetime-string-datetime)
        d2 = datetime.now().strftime("%d/%m/%Y")
        dt_object = datetime.strptime(d2, "%d/%m/%Y")

        # Difference between dates in timedelta
        delta = d1 - dt_object

        return str(delta.days)


# Child class UsefulTips with new parameters
class UsefulTips(Publication):
    def __init__(self, data_type, text_str, body, author):
        super().__init__(data_type, text_str, body)
        self.author = author
        self.body = f'Useful Tips ------------------\n{self.text_str}\nAuthor: ' \
                    f'{self.author.casefold().capitalize().strip()}\n------------------------------'


# New class that take rows(text) from file
class PublFromFile:
    def __init__(self, cnt_sent, filename, path = os.path.join(pathlib.Path.cwd(), 'newsfeed.txt')):
        self.cnt_sent = cnt_sent
        self.filename = filename
        self.path = path

    def read_file(self):
        # Read file
        if self.filename in os.listdir():
            with open(self.path + self.filename, 'r') as f:
                rows_from_file = [str(i) for i in f.readlines()]
                print('Lines successfully read')
                f.close()

            # Remove file
            os.remove(self.path + self.filename)
            print('File successfully deleted ')

            # Create text from file lines according to the number specified by the user
            if self.cnt_sent == 1:
                text_body = ''.join(rows_from_file[:1])
            else:
                text_body = ''.join(rows_from_file[:int(self.cnt_sent)])

            n = text_body
            result = Imported_file.normalization(n)
            return result

        else:
            raise Exception(f'File {self.filename} not founded')


if input('Text from file? Yes/No ').capitalize() == 'No':
    new_publication_object = Publication(input('Choose what you want to publish (News, Private Ad, Useful Tips): ')
                                         .upper().strip(), input('Text: '))
    new_publication_object.publishing()
else:
    new_object = PublFromFile(input('Cnt sentences? '), input('Filename? '))
    text = new_object.read_file()

    new_publication_object = Publication(input('Choose what you want to publish (News, Private Ad, Useful Tips): ')
                                         .upper().strip(), text)
    new_publication_object.publishing()