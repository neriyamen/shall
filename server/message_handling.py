from format import *
from files import FILE
import struct


class MESSAGE_HANDLER:
    def __init__(self):
        self.file = FILE()

    @staticmethod
    def split_message(message):
        message_type, data = b'', b''
        message_type, data = message[:2], message[2:]
        return message_type, data


    def treatment_of_message(self, user, message):
        # choose what to do with any message
        data = ''
        message_type, data = self.split_message(message)
        if message_type == START_SIGN:
            self.start_user(user, data)
        elif message_type == COMMAND_SIGN:
            self.command(user, data)
        elif message_type == UPLOAD_SIGN:
            self.upload(user, data)
        elif message_type == DOWNLOAD_SIGN:
            self.download(user, data)
        elif message_type == EXIT_SIGN:
            self.exit_user(user)
        elif message_type == CD_SIGN:
            self.cd(user, data)
        else:
            print('message is unrecogniz')
            user.send_message(FAILED_MESSAGE)

    def start_user(self, user, data):
        # configure user in first connection.
        user.send_message(START_MESSAGE)

    def exit_user(self, user):
        # care to user who leaving
        user.close()

    def command(self, user, data):
        output = user.user_shell.command(data)
        user.send_message(output)

    def cd(self, user, data):
        user.user_shell.cd(data)

    def upload(self, user, data):
        path, data_len = self.file.unpack_file_properties(data)
        user.send_message(SUCCESS_MESSAGE)
        file_data = user.get_message(data_len)
        self.file.create_file(path, file_data)

    def download(self, user, line):
        path, new_path = line.decode('utf-8').split()
        download_message, file_data = self.file.pack_file_properties(path, new_path)
        user.send_message(download_message)
        answer = user.get_message()
        if answer == SUCCESS_MESSAGE:
            user.send_message(file_data)