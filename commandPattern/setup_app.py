from commands import *
from devices import *
from remote_control import RemoteControlApp


def get_light_commands():
    light = Light()
    return LightOnCommand(light), LightOffCommand(light)


def get_ceiling_fan_high_commands(ceiling_fan):
    return CeilingFanHighCommand(ceiling_fan), CeilingFanOFFCommand(ceiling_fan)


def get_ceiling_fan_medium_commands(ceiling_fan):
    return CeilingFanMediumCommand(ceiling_fan), CeilingFanOFFCommand(ceiling_fan)


def get_ceiling_fan_low_commands(ceiling_fan):
    return CeilingFanLowCommand(ceiling_fan), CeilingFanOFFCommand(ceiling_fan)


def main():
    app = RemoteControlApp()
    light_on, light_off = get_light_commands()
    ceiling_fan = CeilingFan()
    app.set_command(0, *get_light_commands())
    app.set_command(1, *get_ceiling_fan_high_commands(ceiling_fan))
    app.set_command(2, *get_ceiling_fan_medium_commands(ceiling_fan))
    app.set_command(3, *get_ceiling_fan_low_commands(ceiling_fan))
    print('show remote control app information:\n{}'.format(app.command_info))
    print('---- start to push button ----')
    app.push_on_button(0)
    app.push_on_button(1)
    app.push_off_button(0)
    app.push_undo_button()
    app.push_on_button(3)
    app.push_undo_button()
    app.push_off_button(2)


if __name__ == '__main__':
    main()
