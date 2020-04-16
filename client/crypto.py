class CRYPTO:
    # Simple encryption
    def __init__(self):
        self.key = b'1234567'

    def encrypt(self, data):
        # this function using to encryption and decryption
        new_data = b''
        i = 0
        for letter in data:
            new_data += bytes( [letter ^ ord(b'3')])
            i += 1
        return new_data

