from crypto import CRYPTO
BUFFER = 1024

class USER:
    def __init__(self, client_socket, client_shell):
        # create a new user
        self.user_shell = client_shell
        self.user_socket = client_socket
        self.connected = True
        self.crypto =  CRYPTO()

    def send_message(self, data):
        # send message to the user
        self.user_socket.send(self.crypto.encrypt(data))

    def get_message(self, buffer=BUFFER):
        # get message from the user
        try:
            return self.crypto.encrypt(self.user_socket.recv(buffer))
        except:
            if self.connected:
                self.close()

    def close(self):
        if self.connected:
            print(self.user_socket.getpeername(), 'is unconnected')
            self.connected = False
            self.user_socket.close()
