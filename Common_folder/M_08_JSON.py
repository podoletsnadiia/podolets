from datetime import datetime
import os
import json
import pathlib
import M_04_functions as Imported_file

PATH = os.path.join(pathlib.Path.cwd(), 'newsfeed.txt')

# with open('test.json', 'w') as f:
#     f.write(str(a))

# Create parent class with parameters and methods which will be used in every child class
# The 'body' parameter will be overwritten several times and in the final form
# will be equal to the value of the entire publication that will be written to the file


class News:
    def __init__(self):
        self.format_str = myfunc.myfunc()

    def create_news(self, title, main_text):
        city = input('City: ').casefold().capitalize().strip()
        date_time = datetime.now().strftime("%d/%m/%Y, %H:%M")
        main_text = "\n".join([main_text, city, date_time])
        my_news = self.format_str.format_str(title=title, text_body=main_text)
        return my_news


class Publication(News):

    def __init__(self, data_type, text_str='', body=''):
        self.data_type = data_type
        self.text_str = text_str
        self.body = body

    # Function that add body of publication to file
    def write_to_file(self):
        print(f'\nINFO. NewPublicationObject:\n{self.body}')
        try:
            with open(PATH, 'a') as f:
            # with open(os.path.join(self.path, self.filename), 'w') as f:
                f.write(self.body + '\n\n\n')
            print('INFO. Successful. New publication added.')
            return True
        except Exception as e:
            print(f'ERROR. Fail. New publication was not added. Error: {e}')
            return False

    # Function that will create a new 'body'(entire publication) for every type of publication
    def publishing(self):
        def p1():
            return self.create_news(title=self.data_type, main_text=self.text_str)

        def p2():
            return PrivateAd(data_type=self.data_type, text_str=self.text_str, body=self.body).body

        def p3():
            return UsefulTips(data_type=self.data_type, text_str=self.text_str, body=self.body, author=input('Author: ')).body

        try:
            # Create a dict where keys are types of publications, values are functions created above
            self.body = {"NEWS": p1, "PRIVATE AD": p2, "USEFUL TIPS": p3}[
                self.data_type]()  # The function is called right here
        except Exception as e:
            print(f'\nERROR. Incorrect publishing type. Available types (News, Private Ad, Useful Tips). Error: {e}')
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
        self.body = f'News -------------------------\n{self.text_str}\n{self.city.casefold().capitalize().strip()},\
{self.date_time}\n------------------------------'


# Child class PrivateAd with new parameters
class PrivateAd(Publication):
    def __init__(self, data_type, text_str, body):
        super().__init__(data_type, text_str, body)
        self.date_delta = PrivateAd.delta_time(self)
        self.body = f'Private Ad -------------------\n{self.text_str}\nActual until: \
{self.date_delta} days\n------------------------------'

    def delta_time(self):
        str_d1 = input('Please input "Actual until" date in format d/m/Y: ')

        try:
            # Convert string data type to datetime datatype for inputted date
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
        self.body = f'Useful Tips ------------------\n{self.text_str}\nAuthor: \
{self.author.casefold().capitalize().strip()}\n------------------------------'


# New class that take rows(text) from file
class PublFromFile:
    def __init__(self, cnt_sent, filename, path=pathlib.Path.cwd()):
        self.cnt_sent = cnt_sent
        self.filename = filename
        self.path = path

    def read_file(self):
        # Read file
        if self.filename in os.listdir():
            # with open(self.path + self.filename), 'r') as f:
            with open(os.path.join(self.path, self.filename), 'r') as f:
                rows_from_file = [str(i) for i in f.readlines()]
                print('Lines successfully read')

            # Remove file
            os.remove(os.path.join(self.path, self.filename))
            print('File successfully deleted ')

            # Create text from file lines according to the number specified by the user
            if self.cnt_sent == 1:
                text_body = ''.join(rows_from_file[:1])
            else:
                text_body = ''.join(rows_from_file[:int(self.cnt_sent)])

            n = text_body
            result = imported_file.normalization(n)
            return result

        else:
            raise Exception(f'File {self.filename} not founded')


class PublFromJsonFile():
    def __init__(self, count_elements=0, filename='',
                 path=pathlib.Path.cwd()):
        self.count_elements = count_elements
        self.filename = filename
        self.path = path

    def format_text(self, title, body):
        pass

    def body_types(self, f):
        self.format_text(title="News", body="Hi")
        pass

    # def format_str(title, text_body, score=40):
    # tmp_str = title + " " + "-" * (score - len(title) - 1) + "\n"
    # tmp_str += text_body
    # if tmp_str[-1] != '\n':
    # tmp_str += '\n'
    # tmp_str += "-" * score
    # return tmp_str

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
    #   if a in (1, 2, 3):
    #       break
    #   else:
    #       print("number isn't correct")

    # Read file
    def read_json(self):
        if self.filename in os.listdir():

            def body_types(f):
                output_list = []



                for i in range(0, self.count_elements):
                    # element = f[i]
                    if element["Type"].lower() == 'news':
                        body = f"News -------------------------\n{element['Text']}\n{element['City']},\
{element['Date']}\n------------------------------"
                        output_list.append(body)
                    elif element["Type"].lower() == 'privatead':
                        body = f"Private Ad -------------------\n{element['Text']}\nActual until: \
{element['Date']} days\n------------------------------"
                        output_list.append(body)
                    elif element["Type"].lower() == 'usefultips':
                        body = f'Useful Tips ------------------\n{element["Text"]}\nAuthor:\n\
{element["Author"]}\n------------------------------'
                        output_list.append(body)
                    else:
                        raise Exception(f'Type not founded')
                return output_list

            f = json.load(open(os.path.join(self.path, self.filename)))
            if self.count_elements > len(f):
                raise Exception('len file < count elements')
            # else:
            #     return self.count_elements

            # Remove file
            # os.remove(os.path.join(self.path, self.filename))
            print('File successfully deleted ')
            output_list = []
            if f['News']:
                element = f['News']
                if type(f['News']) is not list:
                    element = [element]
                for i in element:
                    text_str = i['text_str']
                    city = i['city']
                    body = f'News -------------------------\n{text_str}\n{city},\
                    {datetime.now().strftime("%d/%m/%Y, %H:%M")}\n------------------------------'
                    print(body)
                    output_list.append(body)
            if f['PrivateAd']:
                element = f['PrivateAd']
                if type(f['PrivateAd']) is not list:
                    element = [element]
                for i in element:
                    text_str = i['text_str']
                    body = f'PrivateAd -------------------------\n{text_str},\
                    {datetime.now().strftime("%d/%m/%Y, %H:%M")}\n------------------------------'
                    print(body)
                    output_list.append(body)
            if f['UsefulTips']:
                element = f['UsefulTips']
                if type(f['UsefulTips']) is not list:
                    element = [element]
                for i in element:
                    text_str = i['text_str']
                    body = f'UsefulTips -------------------------\n{text_str},\
                    {datetime.now().strftime("%d/%m/%Y, %H:%M")}\n------------------------------'
                    print(body)
                    output_list.append(body)

            # str_fin = body_types(f)
            return '\n\n'.join(output_list)

        else:
            raise Exception(f'File {self.filename} not founded')


if __name__ == '__main__':
    if input('Text from file? Yes/No ').capitalize() == 'No':
        new_publication_object = Publication(
            input('Choose what you want to publish (News, Private Ad, Useful Tips): ').upper().strip(), input('Text: '))
        new_publication_object.publishing()
    else:
        if input('JSON? Yes/No ').capitalize() == 'No':
            new_object = PublFromFile(input('Cnt sentences? '), input('Filename? '))
            text_str = new_object.read_file()
            new_publication_object = Publication(
                input('Choose what you want to publish (News, Private Ad, Useful Tips): ').upper().strip(), text)
            new_publication_object.publishing()
        else:
            new_object = PublFromJsonFile(int(input('Cnt sentences? ')), input('Filename? '))
            text_str = new_object.read_json()
            new_publication_object = Publication('', body=text_str)
            new_publication_object.write_to_file()
