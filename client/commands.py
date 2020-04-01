from format import *
from files import FILE

class COMMANDS:
    def __init__(self, connection):
        self.connection = connection
        self.file = FILE()

    def command(self, line):
        self.connection.send_message(COMMAND_SIGN + line.encode())
        print(self.connection.get_message().decode('utf-8'))

    def download(self):
        pass

    def upload(self, line):
        path, new_path = line.split(' ')
        upload_message, file_data = self.file.pack_file_properties(path, new_path)
        self.connection.send_message(UPLOAD_SIGN + upload_message)
        answer = self.connection.get_message()
        if answer == SUCCESS_MESSAGE:
            self.connection.send_message(file_data)

    def download(self, line):
        self.connection.send_message(DOWNLOAD_SIGN + line.encode())
        a = self.connection.get_message()
        print(a)
        data = self.connection.get_message()
        print(data)
        path, data_len = self.file.unpack_file_properties(data)
        self.connection.send_message(SUCCESS_MESSAGE)
        file_data = self.connection.get_message(data_len)
        self.file.create_file(path, file_data)

    def exit(self):
        self.connection.send_message(EXIT_SIGN)
        exit()