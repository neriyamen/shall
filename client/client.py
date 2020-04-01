from connect import CONNECT
from command_line import COMMAND_LINE
from commands import COMMANDS
from format import *

HOST = '127.0.0.1'
 # upload c:\users\base\desktop\hi.txt c:\users\base\desktop\hi2.txt
 # upload c:\users\base\desktop\pic.png c:\users\base\desktop\pic2.png
 # download c:\users\base\desktop\hi.txt c:\users\base\desktop\hi2.txt
class CLIENT:
    def __init__(self):
        self.connection = CONNECT(HOST, PORT)
        self.commands = COMMANDS(self.connection)

    def start_connection(self):
        #open connection with the server
        self.connection.connect_to_server()
        self.connection.send_message(START_SIGN)
        data = self.connection.get_message()

def main():
    client = CLIENT()
    client.start_connection()
    cmd = COMMAND_LINE(client.commands)
    cmd.cmdloop()

if __name__ == '__main__':
    main()
