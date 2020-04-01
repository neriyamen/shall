class CRYPTO:
    def __init__(self):
        self.key = b'1234567'

    def encrypt(self, data):
        new_data = b''
        i = 0
        for letter in data:
            new_data += chr(ord(chr(letter)) ^ 3).encode()
            i += 1
        print('encrypt')
        return new_data

