# from server.user import USER
import user
import connect
import shell
import messagesFormat
import messageHandling
import _thread
import argparse

class SERVER:
    def __init__(self, port):
        """
        remote shell server
        :param port: int type, port to listening
        """
        self.connection = connect.CONNECT(port)
        self.users = []
        self.message_handler = messageHandling.MESSAGE_HANDLER()

    def single_user(self, user):
        """
        thread function for any user
        :param user: USER type, the new user
        """
        while user.connected:
            message = user.get_message()
            if not user.connected:
                break
            self.message_handler.treatment_of_message(user, message)
        user.close()

def parse_arguments():
    """
    parse argument of cli
    :return: int type, port to listening
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', help='Port number to connect to (1-65000)', dest='port', default=messagesFormat.PORT,
                        type=int)
    if legal_port(parser.parse_args().port):
        return parser.parse_args().port
    else:
        exit()

def legal_port(port):
    """
    check the legality of port
    :param port: int type, the selected port
    :return: bool type, is legal port or isn't
    """
    if port > 65000 or port < 1:
        print('illegal port (1-65000)')
        return False
    else:
        return True

def main():
    port = parse_arguments()
    server = SERVER(port)
    server.connection.start_socket_listening()
    while True:
        # establish connection with client
        client_socket, addr = server.connection.socket.accept()
        new_shell = shell.SHELL()
        new_user = user.USER(client_socket, new_shell)
        print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread for one user
        _thread.start_new_thread(server.single_user, (new_user,))
    server.connection.socket.close()

if __name__ == '__main__':
    main()
