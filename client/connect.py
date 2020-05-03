import socket
import crypto

BUFFER_SIZE = 1024

class CONNECT:
    def __init__(self, host, port):
        """
        take care to the connection with the server.
        :param host: string type, host IP
        :param port: int type, host port connection
        :return: none
        """
        self.host = host
        self.port = port
        self.socket = None
        self.crypto = crypto.CRYPTO()

    def connect_to_server(self):
        """
        create socket and make tha first connection with the server.
        :return: none
        """
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
        except ConnectionError as e:
            print (e)
            exit()


    def get_message(self, buffer=BUFFER_SIZE):
        """
        receiver new message from the server.
        :param buffer: int type, buffer of size of data transfer.
        :return:
        """
        try:
            return self.crypto.encrypt(self.socket.recv(buffer))
        except ConnectionError as e:
            print (e)
            exit()

    def send_message(self, data):
        """
        send message to server
        :param data: bytes type, data to send to server
        :return: none
        """
        try:
            self.socket.sendall(self.crypto.encrypt(data))
        except ConnectionError as e:
            print (e)
            exit()
