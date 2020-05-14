import tkinter as tk

from tkinter import ttk, filedialog
from client import physical
from client import data_link
from serial.tools import list_ports
from forms.values import BAUDRATES, BYTESIZES, PARITIES, STOPBITS

cut_port = []
shown_users = []


def cut_port_name(str):
    global cut_port
    for i in range(len(str)):
        cut_port.append(str[i])
        cut_port[i] = str[i].device
    return cut_port


def create_window():
    window = tk.Tk()
    window.title("Setup settings")
    window.geometry("640x480")
    tab_parent = ttk.Notebook(window, width=730, height=400)

    nick_tab = ttk.Frame(tab_parent)
    com_1_tab = ttk.Frame(tab_parent)
    com_2_tab = ttk.Frame(tab_parent)

    tab_parent.add(nick_tab, text="Nick")
    tab_parent.add(com_1_tab, text="COM port 1")
    tab_parent.add(com_2_tab, text="COM port 2")

    # Nick tab setup
    nick_label = tk.Label(nick_tab, text="Nick")
    nick_label.grid(row=1, column=1, padx=20, pady=30)

    nick_value = tk.Entry(nick_tab)
    nick_value.grid(row=1, column=2, padx=20, pady=30)

    # COM 1 port setup

    com_1_port_label = tk.Label(com_1_tab, text="СОМ порт")
    com_1_port_value = ttk.Combobox(com_1_tab)
    ports = list_ports.comports()
    com_1_port_value['values'] = cut_port_name(list_ports.comports())
    com_1_port_value.current(0)

    com_1_speed_label = tk.Label(com_1_tab, text="Скорость")
    com_1_bits_label = tk.Label(com_1_tab, text="Биты данных")
    com_1_stop_label = tk.Label(com_1_tab, text="Стоп биты")
    com_1_even_label = tk.Label(com_1_tab, text="Четность")

    com_1_port_label.grid(row=1, column=1, padx=20, pady=15)
    com_1_speed_label.grid(row=2, column=1, padx=20, pady=15)
    com_1_bits_label.grid(row=3, column=1, padx=20, pady=15)
    com_1_stop_label.grid(row=4, column=1, padx=20, pady=15)
    com_1_even_label.grid(row=5, column=1, padx=20, pady=15)

    # com_1_port_value = tk.Entry(com_1_tab)
    com_1_speed_value = ttk.Combobox(com_1_tab)
    com_1_speed_value['values'] = BAUDRATES
    com_1_speed_value.current(12)

    com_1_bits_value = ttk.Combobox(com_1_tab)
    com_1_bits_value['values'] = BYTESIZES
    com_1_bits_value.current(1)

    com_1_stop_value = ttk.Combobox(com_1_tab)
    com_1_stop_value['values'] = STOPBITS
    com_1_stop_value.current(0)

    com_1_even_value = ttk.Combobox(com_1_tab)
    com_1_even_value['values'] = PARITIES
    com_1_even_value.current(0)

    com_1_port_value.grid(row=1, column=2, padx=20, pady=15)
    com_1_speed_value.grid(row=2, column=2, padx=20, pady=15)
    com_1_bits_value.grid(row=3, column=2, padx=20, pady=15)
    com_1_stop_value.grid(row=4, column=2, padx=20, pady=15)
    com_1_even_value.grid(row=5, column=2, padx=20, pady=15)

    # COM 2 port setup

    com_2_port_label = tk.Label(com_2_tab, text="СОМ порт")
    com_2_port_value = ttk.Combobox(com_2_tab)
    com_2_port_value['values'] = cut_port_name(list_ports.comports())
    com_2_port_value.current(1)

    com_2_speed_label = tk.Label(com_2_tab, text="Скорость")
    com_2_bits_label = tk.Label(com_2_tab, text="Биты данных")
    com_2_stop_label = tk.Label(com_2_tab, text="Стоп биты")
    com_2_even_label = tk.Label(com_2_tab, text="Четность")

    com_2_port_label.grid(row=1, column=1, padx=20, pady=15)
    com_2_speed_label.grid(row=2, column=1, padx=20, pady=15)
    com_2_bits_label.grid(row=3, column=1, padx=20, pady=15)
    com_2_stop_label.grid(row=4, column=1, padx=20, pady=15)
    com_2_even_label.grid(row=5, column=1, padx=20, pady=15)

    com_2_speed_value = ttk.Combobox(com_2_tab)
    com_2_speed_value['values'] = BAUDRATES
    com_2_speed_value.current(12)

    com_2_bits_value = ttk.Combobox(com_2_tab)
    com_2_bits_value['values'] = BYTESIZES
    com_2_bits_value.current(1)

    com_2_stop_value = ttk.Combobox(com_2_tab)
    com_2_stop_value['values'] = STOPBITS
    com_2_stop_value.current(0)

    com_2_even_value = ttk.Combobox(com_2_tab)
    com_2_even_value['values'] = PARITIES
    com_2_even_value.current(0)

    com_2_port_value.grid(row=1, column=2, padx=20, pady=15)
    com_2_speed_value.grid(row=2, column=2, padx=20, pady=15)
    com_2_bits_value.grid(row=3, column=2, padx=20, pady=15)
    com_2_stop_value.grid(row=4, column=2, padx=20, pady=15)
    com_2_even_value.grid(row=5, column=2, padx=20, pady=15)

    def popupmsg(msg):
        popup = tk.Tk()

        def leave():
            popup.destroy()

        popup.wm_title("Error")
        label = ttk.Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        b1 = ttk.Button(popup, text="OK", command=leave)
        b1.pack()
        popup.mainloop()

    def ok_button_click():
        username = nick_value.get()
        if len(username) == 0:
            popupmsg("Введите имя пользователя")
        com_1 = com_1_port_value.get()
        com_2 = com_2_port_value.get()
        window.destroy()
        create_chat_window(username, com_1, com_2)

    tab_parent.pack(expand=1, fill="both")
    tk.Button(window, text='OK', command=ok_button_click).pack(fill=tk.X)

    window.mainloop()


def create_chat_window(username, com_1, com_2):
    chat = tk.Tk()
    chat.geometry("640x480")
    chat.title("Chat, user: " + username)
    global chat_text
    chat_text = tk.Text(chat, width=56, height=18)
    chat_text.grid(row=0, column=0)
    chat_text.insert(tk.END, "Чат с пользователем: <Имя_1> \n")
    chat_text.insert(tk.END, "Имя_1> Привет! \n")
    chat_text.config(state="disabled")
    global users_box
    users_box = tk.Text(chat, width=22, height=18)
    users_box.grid(row=0, column=1)
    # users_box.insert(tk.END, "<Имя_1> \n")
    # users_box.insert(tk.END, "<Имя_2> \n")
    chat_send = tk.Text(chat, width=76, height=2)
    chat_send.grid(row=1, column=0, columnspan=2, rowspan=2)

    def exit():
        physical.button_close(com_1, com_2)
        chat.destroy()

    def save():
        file_path = filedialog.askdirectory()
        if len(file_path) == 0:
            return
        f = open(file_path + "/history.txt", "x")
        text = chat_text.get('1.0', tk.END)
        f.write(text)
        f.close()

    def send():
        text = chat_send.get('1.0', 'end-1c')
        chat_text.config(state="normal")
        msg = username + '> ' + text + ' <Доставлено>' + '\n'
        data_link.send(text)
        chat_text.insert(tk.END, msg)
        chat_text.config(state="disabled")
        data_link.send(msg)
        chat_send.delete('1.0', 'end-1c')

    def connect(e):
        physical.button_open(com_1, com_2, username)
        status.config(text='Статус: Подключение', fg='yellow')
        e.widget.config(state=tk.DISABLED)
        ds.config(state=tk.NORMAL)

    def disconnect(e):
        physical.button_close(com_1, com_2)
        status.config(text='Статус: Отключено', fg='red')
        e.widget.config(state=tk.DISABLED)
        jn.config(state=tk.NORMAL)

    # users_box.tag_config("tag", foreground="#0000ff")
    # users_box.tag_bind("tag", "<Button-1>", lambda e: callback(e, "tag"))
    # users_box.insert(tk.END, '<' + username + '>', "tag")
    users_box.config(state="disabled")
    ds = tk.Button(chat, text="Разъединить", state="disabled")
    ds.bind("<Button-1>", disconnect)
    ds.place(x=160, y=400)
    jn = tk.Button(chat, text="Подключиться", state="normal")
    jn.bind("<Button-1>", connect)
    jn.place(x=10, y=400)
    exit = tk.Button(chat, text="Выход", command=exit).place(x=550, y=400)
    send = tk.Button(chat, text="Отправить", command=send).place(x=400, y=400)
    history = tk.Button(chat, text="История", command=save).place(x=300, y=400)
    status = tk.Label(chat, text='Статус: Отключено', fg='red')
    status.place(x=10, y=370)
    chat.mainloop()


def connected(res):
    users_box.config(state=tk.NORMAL)
    users_box.insert(tk.END, res)
    users_box.config(state=tk.DISABLED)


def receive(decoded):
    chat_text.config(state=tk.NORMAL)
    chat_text.insert(tk.END, 'User' + decoded)
    chat_text.config(state=tk.DISABLED)


def callback(event, tag):
    print(event.widget.get('%s.first' % tag, '%s.last' % tag))


def users_update(users: list):
    global shown_users
    if len(users) != len(shown_users):
        print('users-update', users, shown_users)
        for i in users:
            print(i)
            users_box.config(state=tk.NORMAL)
            users_box.tag_config("tag" + i, foreground="#0000ff")
            users_box.tag_bind("tag" + i, "<Button-1>", lambda e: callback(e, "tag"))
            users_box.insert(tk.END, '<' + i + '>\n', "tag")
            users_box.config(state=tk.DISABLED)
        shown_users = users
