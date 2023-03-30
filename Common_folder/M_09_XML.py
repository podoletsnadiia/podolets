from datetime import datetime
import os
import xml
import json
import pathlib
import M_04_functions as Imported_file

PATH = os.path.join(pathlib.Path.cwd(), 'newsfeed.txt')


class Publication:

    def __init__(self, data_type, text_str='', body=''):
        self.data_type = data_type
        self.text_str = text_str
        self.body = body

    # Function that add body of publication to file
    def write_to_file(self):
        print(f'\nINFO. NewPublicationObject:\n{self.body}')
        try:
            with open(PATH, 'w') as f:
                f.write(self.body + '\n\n\n')
            print('INFO. Successful. New publication added.')
            return True
        except Exception as e:
            print(f'ERROR. Fail. New publication was not added. Error: {e}')
            return False

    # Function that will create a new 'body'(entire publication) for every type of publication
    def publishing(self):
        def p1():
            return News(data_type=self.data_type, text_str=self.text_str, body=self.body, city=input('City: ')).body

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
            with open(self.path + self.filename, 'r') as f:
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
            result = Imported_file.normalization(n)
            return result

        else:
            raise Exception(f'File {self.filename} not founded')


class PublFromJsonFile:
    def __init__(self, count_elements=0, filename='',
                 path=pathlib.Path.cwd()):
        self.count_elements = count_elements
        self.filename = filename
        self.path = path

        # Read file

    def read_json(self):
        if self.filename in os.listdir():
            def check(self, f):
                if self.count_elements > len(f):
                    raise Exception('len file < count elements')
                else:
                    return self.count_elements

            def body_data_types(f):
                output_list = []
                for i in range(0, self.count_elements):
                    element = f[i]
                    if element["data_type"].lower() == 'news':
                        body = f"News -------------------------\n{element['text_str']}\n{element['City']}, " \
                               f"{element['Date']}\n------------------------------"
                        output_list.append(body)
                    elif element["data_type"].lower() == 'private_ad':
                        body = f"Private Ad -------------------\n{element['text_str']}\nActual until: " \
                               f"{element['Date']} days\n------------------------------"
                        output_list.append(body)
                    elif element["data_type"].lower() == 'useful_tips':
                        body = f'Useful Tips ------------------\n{element["text_str"]}\nAuthor: ' \
                               f'{element["Author"]}\n------------------------------'
                        output_list.append(body)
                    else:
                        raise Exception(f'data_type not founded')
                return output_list

            f = json.load(open(f'{self.path}/{self.filename}'))
            check(self, f)

            # Remove file
            os.remove(self.path + self.filename)
            print('File successfully deleted ')

            return '\n\n'.join(body_data_types(f))

        else:
            raise Exception(f'File {self.filename} not founded')


class PublFromXMLFile:
    def __init__(self, count_elements=0, filename='', path=os.path.join(pathlib.Path.cwd())):
        self.count_elements = count_elements
        self.filename = filename
        self.path = path

    def read_xml(self):
        def dict_from_xml():
            with open(self.path + self.filename) as xml_file:
                data_dict = xmltodict.parse(xml_file.read())

            return data_dict

        def body_data_types(data_dict):
            output_list = []
            i = 0
            try:
                for element in data_dict['publication_from_xml']['publication']:
                    i += 1
                    if i > self.count_elements:
                        break

                    if element["type"].lower() == 'news':
                        body = f"News -------------------------\n{element['text_str']}\n{element['city_date']}\n------------------------------"
                        output_list.append(body)
                    elif element["type"].lower() == 'privatead':
                        body = f"Private Ad -------------------\n{element['text_str']}\n{element['date']}\n------------------------------"
                        output_list.append(body)
                    elif element["type"].lower() == 'usefultips':
                        body = f'Useful Tips ------------------\n{element["text_str"]}\n{element["author"]}\n------------------------------'
                        output_list.append(body)
                    else:
                        raise Exception(f'Type not founded')

                # Remove file
                os.remove(self.path + self.filename)
                print('File successfully deleted ')
            except Exception as e:
                print(f'Error: {e}')
                return output_list
            return output_list

        return '\n\n\n'.join(body_data_types(dict_from_xml()))


if __name__ == '__main__':
    if input('Text from file? Yes/No ').capitalize() == 'No':
        new_publication_object = Publication(input('Choose what you want to publish (News, Private Ad, Useful Tips): ').upper().strip(), input('Text: '))
        new_publication_object.publishing()

    else:
        type_of_file = input('JSON/XML/TXT? ').upper()
        if type_of_file == 'JSON':
            new_object = PublFromJsonFile(int(input('Cnt publications? ')), input('Filename? '))
            text_data = new_object.read_json()
            new_publication_object = Publication('', body=text_str)
            new_publication_object.write_to_file()
        elif type_of_file == 'XML':
            new_object = PublFromXMLFile(int(input('Cnt publications? ')), input('Filename? '))
            text_data = new_object.read_xml()
            new_publication_object = Publication('', body=text_str)
            new_publication_object.write_to_file()
        else:
            new_object = PublFromFile(input('Cnt sentences? '), input('Filename? '))
            text_data = new_object.read_file()
            new_publication_object = Publication(input('Choose what you want to publish (News, Private Ad, Useful Tips): ').upper().strip(), text_str)
            new_publication_object.publishing()
