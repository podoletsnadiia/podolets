from datetime import datetime
import pathlib
import os

PATH = os.path.join(pathlib.Path.cwd(), 'newsfeed.txt')
print(PATH)

# Create parent class with parameters and methods which will be used in every child class
# The 'body' parameter will be overwritten several times and in the final form
# will be equal to the value of the entire publication that will be written to the file
class Publication:
    def __init__(self, title, text, body=''):
        self.title = title
        self.text = text
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

# Function that will create a new 'body'(entire publication) for every title of publication
    def publishing(self):
        def p1():
            return News(title=self.title, text=self.text, body=self.body, city=input('City: ')).body

        def p2():
            return PrivateAd(title=self.title, text=self.text, body=self.body).body

        def p3():
            return UsefulTips(title=self.title, text=self.text, body=self.body, author=input('Author: ')).body

        try:
            # Create a dict where keys are titles of publications, values are functions created above
            self.body = {"NEWS": p1, "PRIVATE AD": p2, "USEFUL TIPS": p3}[self.title]()  # The function is called right here
        except Exception as e:
            print(f'\nERROR. Incorrect publishing title. Available titles (News, Private Ad, Useful Tips). Error: {e}')
            return False

# Call other method-function of the class from here
        return True if Publication.write_to_file(self) else False

# Child class News with new parameters
class News(Publication):
    def __init__(self, text, title, city, body, date_time=datetime.now().strftime("%d/%m/%Y, %H:%M")):
        # The super() function is used to give access to methods and properties of a parent class.
        super().__init__(title, text, body)
        self.city = city
        self.date_time = date_time
        self.body = f'News -------------------------\n{self.text}\n{self.city.casefold().capitalize().strip()}, {self.date_time}\n------------------------------'




# Child class PrivateAd with new parameters
class PrivateAd(Publication):
    def __init__(self, title, text, body, delta_time=''):
        super().__init__(title, text, body)
        self.date_delta = PrivateAd.delta_time(self)
        self.body = f'Private Ad -------------------\n{self.text}\nActual until: {self.date_delta} days\n------------------------------'

    def delta_time(self):
        while True:
            str_d1 = input('Please input "Actual until" date in format d/m/Y: ')

            try:
            # Convert string data title to datetime datatype for inputted date
                d1 = datetime.strptime(str_d1, "%d/%m/%Y")
                break
            except Exception as e:
                print(f'ERROR. Enter date in followed format next time: d/m/Y. Error: {e}')


# Double conversion for publishing date (datetime-string-datetime)
        d2 = datetime.now().strftime("%d/%m/%Y")
        dt_object = datetime.strptime(d2, "%d/%m/%Y")

        # Difference between dates in timedelta
        delta = d1 - dt_object

        return str(delta.days)

# Child class UsefulTips with new parameters
class UsefulTips(Publication):
    def __init__(self, title, text, body, author):
        super().__init__(title, text, body)
        self.author = author
        self.body = f'Useful Tips ------------------\n{self.text}\nAuthor: {self.author.casefold().capitalize().strip()}\n------------------------------'

# def format_str(title, body, score=50):
#     tmp_str = title + " " + "-" * (score - len(title) - 1) + "\n"
#     tmp_str += body
#     if tmp_str[-1] != '\n':
#         tmp_str += '\n'
#     tmp_str += "-" * score
#     return tmp_str
#
# print(format_str("UsefulTips", "hello"))

new_publication_object = Publication(input('Choose what you want to publish (News, Private Ad, Useful Tips): ').upper().strip(), input('Text: '))
new_publication_object.publishing()

# while True:
#     print('Choose what you want to publish:\n1 - News\n2 - Private Ad\n3 - Useful Tips\n\n0 - Exit\n')
#     a = input('Select number: ')
#     if a == '1':
#         print("Call class News")
#     elif a == '2':
#         print("Call class Private Ad")
#     elif a == '3':
#         print("Call class Useful Tips")
#     elif a == '0':
#         exit()