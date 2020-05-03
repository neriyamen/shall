class CRYPTO:
    def __init__(self):
        self.key = b'1234567'

    def encrypt(self, data):
        """
        this function using to encryption and decryption
        :param data: bytes type, data to encrypt/discrypt
        :return: bytes type, data after encrypt/discrypt
        """
        new_data = b''
        i = 0
        for letter in data:
            new_data += bytes( [letter ^ ord(b'3')])
            i += 1
        return new_data

