from forms import entry
import _thread
import threading


def main():
    threading.Thread(target=entry.create_window, daemon=False).start()


if __name__ == "__main__":
    main()
