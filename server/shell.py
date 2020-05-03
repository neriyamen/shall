import subprocess

class SHELL:
    def __init__(self):
        """
        simple remote shell options
        """
        self.path = 'C:\\'

    def command(self, command):
        """
        simple command
        :param command: bytes type, command to run on the server
        :return: bytes type, output of command
        """
        try:
            output = subprocess.check_output(command.decode('utf-8'), shell=True, cwd=self.path)
            if output == '':
                output = b'success'
        except:
            output = b'faild'
        return output

    def cd(self, line):
        """
        cd in remote shell
        :param line: new path
        """
        if line in subprocess.check_output('dir', shell=True, cwd=self.path):
            self.path += '\\' + line.decode('utf-8')
