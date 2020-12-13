class Light():
    def on(self):
        print('light on')

    def off(self):
        print('light off')


class CeilingFan():
    HIGH = 3
    MEDIUM = 2
    LOW = 1

    def __init__(self):
        self.speed = 'OFF'

    def get_speed(self):
        return self.speed

    def high(self):
        print('ceiling fan turn speed {} to {}'.format(self.speed, self.HIGH))
        self.speed = self.HIGH

    def medium(self):
        print('ceiling fan turn speed {} to {}'.format(self.speed, self.MEDIUM))
        self.speed = self.MEDIUM

    def low(self):
        print('ceiling fan turn speed {} to {}'.format(self.speed, self.LOW))
        self.speed = self.LOW

    def off(self):
        print('ceiling fan turn speed {} to off'.format(self.speed))
        self.speed = 'OFF'
