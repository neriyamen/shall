import crypto

BUFFER = 1024

class USER:
    def __init__(self, client_socket, client_shell):
        """
        create a new user
        :param client_socket: socket object, socket of the connection with the new user
        :param client_shell: SHELL object, the shell of the new user
        """
        self.user_shell = client_shell
        self.user_socket = client_socket
        self.connected = True
        self.crypto = crypto.CRYPTO()

    def send_message(self, data):
        """
        send message to the user
        :param data: bytes type, the message
        :return: none
        """
        try:
            self.user_socket.send(self.crypto.encrypt(data))
        except ConnectionError as e:
            print (self.user_socket.getpeername(), ':', e)
            if self.connected:
                self.close()

    def get_message(self, buffer=BUFFER):
        """
        get message from the user
        :param buffer: int type, buffer of get message size
        :return: bytes type, message from the server
        """
        try:
            return self.crypto.encrypt(self.user_socket.recv(buffer))
        except ConnectionError as e:
            print (self.user_socket.getpeername(), ':', e)
            if self.connected:
                self.close()

    def close(self):
        """
        close connection with user
        :return: none
        """
        if self.connected:
            print(self.user_socket.getpeername(), 'is unconnected')
            self.connected = False
            self.user_socket.close()
