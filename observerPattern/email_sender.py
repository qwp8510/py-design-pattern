from email_interface import EmailInterface
import json


class EmailSender(EmailInterface):
    def __init__(self):
        self.forms = []

    def register_subject(self, form):
        self.forms.append(form)

    def remove_subject(self, form):
        self.forms.remove[form]

    def send(self, message):
        forms = self.forms
        for form in forms:
            try:
                form.send(message)
            except Exception as err:
                print('Error: EmailSender send fail with {}'.format(err))

    @property
    def content(self):
        with open('./info.json', 'r') as js:
            content = json.load(js)
            js.close()
        return content

    def update_message(self):
        self.send(self.content)
