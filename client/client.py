import connect
import commandLine
import commands
import messagesFormat

HOST = '127.0.0.1'

class CLIENT:
    def __init__(self):
        """
        this class containing the properties of client and connection's properties
        """
        self.connection = connect.CONNECT(HOST, messagesFormat.PORT)
        self.commands = commands.COMMANDS(self.connection)

    def start_connection(self):
        """
        open connection with the server
        """
        self.connection.connect_to_server()
        self.connection.send_message(messagesFormat.START_SIGN)
        data = self.connection.get_message()

def main():
    client = CLIENT()
    client.start_connection()
    cmd = commandLine.COMMAND_LINE(client.commands)
    cmd.cmdloop()

if __name__ == '__main__':
    main()
