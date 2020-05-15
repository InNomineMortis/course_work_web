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
    res = str.encode('PERM,' + nick + '\r')
    time.sleep(1)
    if port_2.port == '/dev/ttyS20' or port_2.port == 'COM2':
        port_2.write(res)
        print('sent', res)
    print(port_1, 'com_1: ', com_1)
    print(port_2, 'com_2: ', com_2)
    global thread
    thread = threading.Thread(target=check_connection, args=(nick,), daemon=True)
    time.sleep(1)
    thread.start()


def button_close():
    global user_list
    user_list = []
    try:
        port_2.write(str.encode('DOWNLINK\r'))
    except serial.portNotOpenError:
        print(port_1)
        print(port_2)
        return

    try:
        port_1.close()
        port_2.close()
    except serial.portNotOpenError:
        print(port_1)
        print(port_2)


user_list = []


def check_connection(username):
    global user_list
    users_list = []
    count = 0
    flag = False
    same = False
    print('In thread', port_1)
    while True:
        strs = ''
        users_str = ''
        time.sleep(5)
        print(port_1.is_open, port_2.is_open)
        if not port_1.is_open or count == 6:
            port_1.close()
            port_2.close()
            entry.disconnected()
            break
        while True:
            reading = port_1.read(1)
            if reading == b'\r' or reading == b'':
                break
            else:
                strs += reading.decode()
        print_data('got:', strs)
        if len(strs) != 0:
            count = 0
            if strs[0:4] == 'PERM':
                users = strs.split(',')
                try:
                    users.index(username)
                except ValueError:
                    users.append(username)
                print('users in phys:', users)
                if len(users) != len(users_list):
                    users_list = users.copy()
                    flag = True
                    del users[0]
                    entry.users_update(users)
                else:
                    same = True
            if strs[0:8] == 'DOWNLINK':
                port_2.write(str.encode(strs + '\r'))
                port_2.close()
                port_1.close()
                entry.disconnected()
                break
            if strs[0:4] == "DATA":
                encoded = strs.split(',')
                res = data_link.decode(encoded[1])
                res = res.split(',')
                print(res)
                if res[0] == username:
                    port_2.write(str.encode("ASK," + username + ',' + res[1] + '\r'))
                    entry.receive(res)
                else:
                    port_2.write(str.encode(strs + '\r'))
            if strs[0:3] == 'ASK':
                encoded = strs.split(',')
                if encoded[2] == username:
                    entry.change_status(encoded[1])
                else:
                    port_2.write(str.encode(strs + '\r'))

        print('user-list', users_list)
        if same:
            same = False
            port_2.write(str.encode(strs + '\r'))
        elif flag:
            for i in users_list:
                flag = False
                users_str += i + ','
            users_str = users_str[0:len(users_str) - 1]
            print(users_str)
            port_2.write(str.encode(users_str + '\r'))
        else:
            count += 1
        print('count: ', count)


def print_data(data, data_1):
    print(data, data_1)


def send(encoded):
    print('sending', str.encode(encoded + '\r'))
    res = str.encode('DATA,' + encoded + '\r')
    time.sleep(0.1)
    port_2.write(res)
    print('sent')
