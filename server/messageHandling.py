import messagesFormat
from files import FILE

class MESSAGE_HANDLER:
    def __init__(self):
        self.file = FILE()

    @staticmethod
    def split_message(message):
        """
        split a message from the client to message type and data
        :param message: bytes type, full message (type and data)
        :return: tuple (bytes, bytes) - (message type, data)
        """
        message_type, data = b'', b''
        message_type, data = message[:2], message[2:]
        return message_type, data


    def treatment_of_message(self, user, message):
        """
        choose what to do with any message
        :param user: USER type, user who send the message
        :param message: bytes type, the message
        :return: none
        """
        data = ''
        message_type, data = self.split_message(message)
        if message_type == messagesFormat.START_SIGN:
            user.send_message(messagesFormat.START_MESSAGE)
        elif message_type == messagesFormat.COMMAND_SIGN:
            self.command(user, data)
        elif message_type == messagesFormat.UPLOAD_SIGN:
            self.upload(user, data)
        elif message_type == messagesFormat.DOWNLOAD_SIGN:
            self.download(user, data)
        elif message_type == messagesFormat.EXIT_SIGN:
            user.close()
        elif message_type == messagesFormat.CD_SIGN:
            user.user_shell.cd(data)
        else:
            print('message is unrecogniz')
            user.send_message(messagesFormat.FAILED_MESSAGE)

    def command(self, user, data):
        """
        'command' option
        :param user: USER type, owner of the message
        :param data: bytes type, the command
        :return: none
        """
        output = user.user_shell.command(data)
        user.send_message(output)

    def upload(self, user, data):
        """
        upload files *from user* *to server*
        :param user: USER type, owner of the message
        :param data: bytes type, file properties
        :return: none
        """
        path, data_len = self.file.unpack_file_properties(data)
        user.send_message(messagesFormat.SUCCESS_MESSAGE)
        file_data = user.get_message(data_len)
        self.file.create_file(path, file_data)

    def download(self, user, line):
        """
        download file *from server* *to client*
        :param user: USER type, owner of message
        :param line: bytes type, file properties
        :return: none
        """
        path, new_path = line.decode('utf-8').split()
        download_message, file_data = self.file.pack_file_properties(path, new_path)
        user.send_message(download_message)
        answer = user.get_message()
        if answer == messagesFormat.SUCCESS_MESSAGE:
            user.send_message(file_data)