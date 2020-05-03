import messagesFormat
import files

class COMMANDS:
    def __init__(self, connection):
        """
        all actions between client and socket
        :param connection: CONNECT class type, the connection between server and client
        """
        self.connection = connection
        self.file = files.FILE()

    def command(self, line):
        """
        "command" is for simple cli command like 'dir' or 'netstat -nat'
        :param line: string type, command to send to server
        :return: string type, answer from the server
        """
        self.connection.send_message(messagesFormat.COMMAND_SIGN + line.encode())
        answer = self.connection.get_message(100000)
        try:
            return answer.decode('unicode_escape')
        except:
            return answer.decode('utf-8')

    def upload(self, line):
        """
        upload file (from the client to the server)
        :param line: string type, properties of the file (path and new path)
        :return: none
        """
        path, new_path = line.split(' ')
        upload_message, file_data = self.file.pack_file_properties(path, new_path)
        self.connection.send_message(messagesFormat.UPLOAD_SIGN + upload_message)
        answer = self.connection.get_message()
        if answer == messagesFormat.SUCCESS_MESSAGE:
            print('upload file...')
            self.connection.send_message(file_data)

    def download(self, line):
        """
        download file (from the server to the client)
        :param line: string type, properties of the file (path and new path)
        :return: none
        """
        self.connection.send_message(messagesFormat.DOWNLOAD_SIGN + line.encode())
        data = self.connection.get_message()
        path, data_len = self.file.unpack_file_properties(data)
        self.connection.send_message(messagesFormat.SUCCESS_MESSAGE)
        file_data = self.connection.get_message(data_len)
        self.file.create_file(path, file_data)

    def cd(self, line):
        """
        cd in the server
        :param line: string type, new path
        :return: none
        """
        self.connection.send_message(messagesFormat.CD_SIGN + line.encode())

    def super(self):
        """
        super command, print some importent properties of server
        :return: none
        """
        ipconfig = self.command('ipconfig')
        netstat = self.command('netstat -nat')
        print(ipconfig, netstat)

    def exit(self):
        """
        exit from the client
        :return: none
        """
        self.connection.send_message(messagesFormat.EXIT_SIGN)
        exit()