from forms import *
from email_sender import EmailSender
import json


FORMS = {'employee': EmployForms, 'manager': ManagerForms}


def get_employee_content():
    with open('./employee.json', 'r') as js:
        content = json.load(js)
        js.close()
    return content


def main():
    email_sender = EmailSender()
    for name, data in get_employee_content().items():
        try:
            form = FORMS.get(data.get('level'), NotExistLevelForms)
            form(name, email_sender)
        except Exception as err:
            print('Error: Main fail with {}'.format(err))     
    email_sender.update_message()


if __name__ == '__main__':
    main()
