import cmd


class COMMAND_LINE(cmd.Cmd):
    """Simple command processor example."""
    def __init__(self, commands):
        cmd.Cmd.__init__(self)
        self.commands = commands

    def do_command(self, line):
        self.commands.command(line)

    def do_upload(self, line):
        self.commands.upload(line)

    def do_download(self, line):
        self.commands.download(line)

    def do_exit(self, line):
        self.commands.exit()
