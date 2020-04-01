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
        try:
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
        except:
            print('message is unrecogniz')
            user.send_message(FAILED_MESSAGE)

    def start_user(self, user, data):
        # configure user in first connection.
        user.send_message(START_MESSAGE)

    def exit_user(self, user):
        # care to user who leaving
        user.close()
        # self.users.remove(user)

    def command(self, user, data):
        output = user.user_shell.command(data)
        user.send_message(output)

    def upload(self, user, data):
        path, data_len = self.file.unpack_file_properties(data)
        user.send_message(SUCCESS_MESSAGE)
        file_data = user.get_message(data_len)
        self.file.create_file(path, file_data)

    def download(self, user, line):
        print(line)
        path, new_path = line.split(' ')
        # user.send_message(SUCCESS_MESSAGE)
        download_message, file_data = self.file.pack_file_properties(path, new_path)
        print(download_message)
        user.send_message(download_message)
        answer = user.get_message()
        if answer == SUCCESS_MESSAGE:
            user.send_message(file_data)