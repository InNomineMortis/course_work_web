import tkinter as tk

from tkinter import ttk


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
    com_1_speed_label = tk.Label(com_1_tab, text="Скорость")
    com_1_bits_label = tk.Label(com_1_tab, text="Биты данных")
    com_1_stop_label = tk.Label(com_1_tab, text="Стоп биты")
    com_1_even_label = tk.Label(com_1_tab, text="Четность")

    com_1_port_label.grid(row=1, column=1, padx=20, pady=15)
    com_1_speed_label.grid(row=2, column=1, padx=20, pady=15)
    com_1_bits_label.grid(row=3, column=1, padx=20, pady=15)
    com_1_stop_label.grid(row=4, column=1, padx=20, pady=15)
    com_1_even_label.grid(row=5, column=1, padx=20, pady=15)

    com_1_port_value = tk.Entry(com_1_tab)
    com_1_speed_value = tk.Entry(com_1_tab)
    com_1_bits_value = tk.Entry(com_1_tab)
    com_1_stop_value = tk.Entry(com_1_tab)
    com_1_even_value = tk.Entry(com_1_tab)

    com_1_port_value.grid(row=1, column=2, padx=20, pady=15)
    com_1_speed_value.grid(row=2, column=2, padx=20, pady=15)
    com_1_bits_value.grid(row=3, column=2, padx=20, pady=15)
    com_1_stop_value.grid(row=4, column=2, padx=20, pady=15)
    com_1_even_value.grid(row=5, column=2, padx=20, pady=15)

    # COM 2 port setup

    com_2_port_label = tk.Label(com_2_tab, text="СОМ порт")
    com_2_speed_label = tk.Label(com_2_tab, text="Скорость")
    com_2_bits_label = tk.Label(com_2_tab, text="Биты данных")
    com_2_stop_label = tk.Label(com_2_tab, text="Стоп биты")
    com_2_even_label = tk.Label(com_2_tab, text="Четность")

    com_2_port_label.grid(row=1, column=1, padx=20, pady=15)
    com_2_speed_label.grid(row=2, column=1, padx=20, pady=15)
    com_2_bits_label.grid(row=3, column=1, padx=20, pady=15)
    com_2_stop_label.grid(row=4, column=1, padx=20, pady=15)
    com_2_even_label.grid(row=5, column=1, padx=20, pady=15)

    com_2_port_value = tk.Entry(com_2_tab)
    com_2_speed_value = tk.Entry(com_2_tab)
    com_2_bits_value = tk.Entry(com_2_tab)
    com_2_stop_value = tk.Entry(com_2_tab)
    com_2_even_value = tk.Entry(com_2_tab)

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
        window.destroy()
        create_chat_window(username)

    tab_parent.pack(expand=1, fill="both")
    tk.Button(window, text='OK', command=ok_button_click).pack(fill=tk.X)

    window.mainloop()


def create_chat_window(username):
    chat = tk.Tk()
    chat.geometry("640x480")
    chat.title("Chat, user: " + username)
    chat_text = tk.Text(chat, width=56, height=18)
    chat_text.grid(row=0, column=0)
    chat_text.config(state="disabled")
    users_box = tk.Text(chat, width=22, height=18)
    users_box.grid(row=0, column=1)
    users_box.config(state="disabled")
    chat_send = tk.Text(chat, width=76, height=2)
    chat_send.grid(row=1, column=0, columnspan=2)
    tk.Button(chat, text="Разёединить")
    chat.mainloop()
