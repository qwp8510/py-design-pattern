from commands import UnknownCommand


class RemoteControlApp():
    max_size = 10

    def __init__(self):
        self.on_commands, self.off_commands = [], []
        self.undo_command = ''
        self.set_init_command()

    def set_init_command(self):
        unknown_command = UnknownCommand()
        for _ in range(self.max_size):
            self.on_commands.append(unknown_command)
            self.off_commands.append(unknown_command)
        self.undo_command = unknown_command

    @property
    def command_info(self):
        info = []
        for order in range(len(self.on_commands)):
            info.append('[order {}] App commands already set on: {}, off: {}'.format(
                order,
                self.on_commands[order].__class__.__name__,
                self.off_commands[order].__class__.__name__
            ))
        return '\n'.join(info)

    def set_command(self, order, on_command, off_command):
        self.on_commands[order] = on_command
        self.off_commands[order] = off_command

    def push_on_button(self, order):
        self.on_commands[order].execute()
        self.undo_command = self.on_commands[order]

    def push_off_button(self, order):
        self.off_commands[order].execute()
        self.undo_command = self.off_commands[order]

    def push_undo_button(self):
        self.undo_command.undo()
