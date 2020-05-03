import cmd

class COMMAND_LINE(cmd.Cmd):
    def __init__(self, commands):
        """
        Simple command processor example.
        :param commands: COMMANDS class type,
        :return: none
        """
        cmd.Cmd.__init__(self)
        self.commands = commands

    def do_command(self, line):
        """
        command is the option to send a simple command to shell (like 'dir')
        :param line: string type,
        :return: none
        """
        print(self.commands.command(line))

    def do_upload(self, line):
        """
        upload file (from the client to the server)
        :param line: string type, properties of the file (path and new path)
        :return: none
        """
        self.commands.upload(line)

    def do_download(self, line):
        """
        download file (from the server to the client)
        :param line: string type, properties of the file (path and new path)
        :return: none
        """
        self.commands.download(line)

    def do_cd(self, line):
        """
        cd in the server
        :param line: string type, new path
        :return: none
        """
        self.commands.cd(line)

    def do_super(self, line):
        """
        super command, print some importent properties of server
        :param line: string type, not used - is for cmd.cmd class
        :return: none
        """
        self.commands.super()

    def do_exit(self, line):
        """
        exit from the client
        :param line: string type, not used - is for cmd.cmd class
        :return: none
        """
        self.commands.exit()
