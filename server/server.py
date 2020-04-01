from user import USER
from connect import CONNECT
from shell import SHELL
from format import *
from message_handling import MESSAGE_HANDLER
from files import FILE
from _thread import *

class SERVER:
    def __init__(self, port):
        self.connection = CONNECT(port)
        self.users = []
        self.message_handler = MESSAGE_HANDLER()


    def single_user(self, user):
        # thread function for any user
        while user.connected:
            message = user.get_message()
            if not user.connected:
                break
            self.message_handler.treatment_of_message(user, message)
        user.close()

def main():
    server = SERVER(PORT)
    server.connection.start_socket_listening()
    while True:
        # establish connection with client
        client_socket, addr = server.connection.socket.accept()
        new_shell = SHELL()
        user = USER(client_socket, new_shell)
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread for one user
        start_new_thread(server.single_user, (user,))
    server.connection.socket.close()

if __name__ == '__main__':
    main()
