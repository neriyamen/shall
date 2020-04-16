from format import *
from files import FILE

class COMMANDS:
    # all actions between client and socket
    def __init__(self, connection):
        self.connection = connection
        self.file = FILE()

    def command(self, line):
        # "command" is for simple cli command like 'dir' or 'netstat -nat'
        self.connection.send_message(COMMAND_SIGN + line.encode())
        answer = self.connection.get_message(100000)
        try:
            return answer.decode('unicode_escape')
        except:
            return answer.decode('utf-8')

    def upload(self, line):
        # 'upload' is for transfer files from client to server
        path, new_path = line.split(' ')
        upload_message, file_data = self.file.pack_file_properties(path, new_path)
        self.connection.send_message(UPLOAD_SIGN + upload_message)
        answer = self.connection.get_message()
        if answer == SUCCESS_MESSAGE:
            self.connection.send_message(file_data)

    def download(self, line):
        # 'download' is for transfer files from server to client
        self.connection.send_message(DOWNLOAD_SIGN + line.encode())
        data = self.connection.get_message()
        path, data_len = self.file.unpack_file_properties(data)
        self.connection.send_message(SUCCESS_MESSAGE)
        file_data = self.connection.get_message(data_len)
        self.file.create_file(path, file_data)

    def cd(self, line):
        # change path in server
        self.connection.send_message(CD_SIGN + line.encode())

    def super(self):
        # summary of important information about server
        ipconfig = self.command('ipconfig')
        netstat = self.command('netstat -nat')
        print(ipconfig, netstat)



    def exit(self):
        self.connection.send_message(EXIT_SIGN)
        exit()