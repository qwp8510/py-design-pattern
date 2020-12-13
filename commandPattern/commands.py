from base_command import Command


class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()


class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()


class CeilingFanHighCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = 'OFF'

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.high()

    def undo(self):
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class CeilingFanMediumCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = 'OFF'

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.medium()

    def undo(self):
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class CeilingFanLowCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan
        self.prev_speed = 'OFF'

    def execute(self):
        self.prev_speed = self.ceiling_fan.get_speed()
        self.ceiling_fan.low()

    def undo(self):
        if self.prev_speed == self.ceiling_fan.HIGH:
            self.ceiling_fan.high()
        elif self.prev_speed == self.ceiling_fan.MEDIUM:
            self.ceiling_fan.medium()
        elif self.prev_speed == self.ceiling_fan.LOW:
            self.ceiling_fan.low()
        else:
            self.ceiling_fan.off()


class CeilingFanOFFCommand(Command):
    def __init__(self, ceiling_fan):
        self.ceiling_fan = ceiling_fan

    def execute(self):
        self.ceiling_fan.off()

    def undo(self):
        self.ceiling_fan.off()


class UnknownCommand(Command):
    def execute(self):
        print('Not yet set up command')

    def undo(self):
        print('Not yet set up command')
