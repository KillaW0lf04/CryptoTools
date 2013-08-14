__author__ = 'Michael Aquilina'

# Encrypt and decrypt messages using the AES block cipher!
# aes.py <message> <passphrase> --encode
# aes.py <message> <passphrase> --decode

# Perform preliminary check for dependencies
import sys
import pkg_resources
from distutils.version import StrictVersion

MIN_REQUIRED_VERSION = '2.6'

# Ensure an up to date version of PyCrypto is installed before continuing
try:
    pycrypto_version = pkg_resources.get_distribution('PyCrypto').version
except pkg_resources.DistributionNotFound:
    installed = False
else:
    installed = StrictVersion(pycrypto_version) >= StrictVersion(MIN_REQUIRED_VERSION)

if not installed:
    print 'You require PyCrypto version %s or later to use this tool' % MIN_REQUIRED_VERSION
    print 'Download it from https://www.dlitz.net/software/pycrypto/'
    sys.exit(1)

from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF1

from Crypto import Random


def encode_message(key, plaintext, key_size=16):

    # Generate a random Initialisation Vector
    prng = Random.new()
    iv = prng.read(AES.block_size)

    AES.key_size = key_size
    cipher = AES.new(key, AES.MODE_CFB, iv)

    return iv + cipher.encrypt(plaintext)


def decode_message(key, ciphertext, key_size=16):
    iv = ciphertext[:AES.block_size]
    ct = ciphertext[AES.block_size:]

    AES.key_size = key_size
    cipher = AES.new(key, AES.MODE_CFB, iv)

    return cipher.decrypt(ct)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Encode or Decode messages using the Advanced Encryption Standard (AES).')
    parser.add_argument('--encode', '-e', action='store_true', help='Perform encryption of the incoming message. Input text is expected in ASCII format.')
    parser.add_argument('--decode', '-d', action='store_true', help='Perform decryption of the incoming message. Input text is expected in hex encoded format.')
    parser.add_argument('text', help='The text to encode or decode depending on the function being used.')
    parser.add_argument('passphrase', help='Specify the passphrase with which to generate the cipher key.')
    parser.add_argument('--salt', '-s', help='Specify the salt to use when deriving a key from your passphrase.', default='12345678')
    parser.add_argument('--key-size', type=int, choices=(16, 24, 32), default=16, help='Specify the key size (16, 24 or 32 bytes). Default is 16 bytes.')

    # Parse the command line arguments
    args = parser.parse_args()

    # Derive a key using a key derivation function
    key = PBKDF1(args.passphrase, args.salt, args.key_size)

    if args.encode:
        ciphertext = encode_message(key, args.text, args.key_size)
        print 'Your encoded ciphertext is (in hex format):'
        print ciphertext.encode('hex')

    elif args.decode:
        # Convert hex encoded message into ciphertext (ascii)
        ciphertext = args.text.decode('hex')

        print 'Your decoded plaintext is:'
        print decode_message(key, ciphertext, args.key_size)
    else:
        print 'Please specify whether you wish to --encode or --decode'
        sys.exit(1)
