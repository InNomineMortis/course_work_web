import serial
import forms.values as value


def button_open():
    pc = serial.Serial()
    pc.port = value.DEFAULT_PORT_1
    pc.open()
    pc.port = value.DEFAULT_PORT_2
    pc.open()


def input(text):
    pc = serial.Serial()
    pc.write()
