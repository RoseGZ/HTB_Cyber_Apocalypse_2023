from os import urandom
from Crypto.Cipher import AES



MESSAGE = "secret message"
assert all([x.isupper() or x in '{_} ' for x in MESSAGE])


class Cipher:

    def __init__(self):
        self.salt = urandom(15)
        print(self.salt)
        key = urandom(16)
        print(key)
        self.cipher = AES.new(key, AES.MODE_ECB)
        print(self.salt)
        print(key)

    def encrypt(self, message):
        return [self.cipher.encrypt(c.encode() + self.salt) for c in message]


def main():
    cipher = Cipher()
    encrypted = cipher.encrypt(MESSAGE)
    encrypted = "\n".join([c.hex() for c in encrypted])

    with open("output.txt", 'w+') as f:
        f.write(encrypted)


if __name__ == "__main__":
    main()
