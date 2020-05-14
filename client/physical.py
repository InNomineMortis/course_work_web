import io
import time
import serial
from forms import entry
import threading
from multiprocessing.pool import ThreadPool
from client import data_link


def button_open(com_1, com_2, nick):
    global port_1, port_2
    port_1 = serial.Serial(timeout=0)
    port_2 = serial.Serial(timeout=0)
    port_1.port = com_1
    port_2.port = com_2
    # port_2.setDTR(True)
    # port_1.setDTR(True)
    port_1.open()
    port_2.open()
    res = str.encode('users,' + nick + '\r')
    time.sleep(1)
    port_2.write(res)
    print(port_1, 'com_1: ', com_1)
    print(port_2, 'com_2: ', com_2)
    global thread
    thread = threading.Thread(target=check_connection, args=(nick,))
    thread.start()


def button_close(com_1, com_2):
    port_1 = serial.Serial()
    port_2 = serial.Serial()
    port_1.port = com_1
    port_2.port = com_2
    port_1.close()
    port_2.close()
    print(port_1)
    print(port_2)


def check_connection(username):
    users_list = []
    flag = False
    users_str = 'users'
    strs = ''
    while True:
        time.sleep(5)
        while True:
            reading = port_1.read(1)
            if reading == b'\r':
                break
            else:
                strs += reading.decode()
        print_data('got:', strs)
        if len(strs) != 0:
            if strs[0:5] == 'users':
                users = strs.split(',')
                try:
                    users.index(username)
                except ValueError:
                    users.append(username)
                print(users)
                if len(users) != len(users_list):
                    users_list = users
                    flag = True
                    del users[0]
                    entry.users_update(users)
        print('user-list', users_list)
        if flag:
            for i in users_list:
                users_str += ',' + i
            print(users_str)
            port_2.write(str.encode(users_str))
        else:
            port_2.write(str.encode(users_str + ',' + username))


def print_data(data, data_1):
    print(data, data_1)


def send(encoded):
    print('sending', str.encode(encoded + '\r'))
    res = str.encode(encoded + '\r')
    time.sleep(0.1)
    port_2.write(res)
    print('sent')
