from forms_interface import FormsInterface


class EmployForms(FormsInterface):
    not_employ_message = ['watch-list']

    def __init__(self, name, sender):
        self.name = name
        sender.register_subject(self)

    def send(self, msg):
        """ Implement sending email """
        def get_employee_msg():
            update_msg = msg.copy()
            for field in self.not_employ_message:
                del update_msg[field]
            return update_msg

        print('sending to employee {} message : {}'.format(self.name, get_employee_msg()))


class ManagerForms(FormsInterface):
    def __init__(self, name, sender):
        self.name = name
        sender.register_subject(self)

    def send(self, msg):
        """ Implement sending email """
        print('sending to manager {} message : {}'.format(self.name, msg))


class NotExistLevelForms(FormsInterface):
    def __init__(self, name, sender):
        self.name = name
        sender.register_subject(self)

    def send(self, msg):
        """ Implement sending email """
        raise '{} fail with sending, due to unfind level {}'.format(self.name)
