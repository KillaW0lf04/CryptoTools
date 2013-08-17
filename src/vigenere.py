# -*- coding: utf8 -*-

__author__ = 'Michael Aquilina'

# Encrypt and Decrypt messages with the Vigenère Cipher. This is a historic
# cipher which was used during the renaissance and is often thought to be
# the natural successor to the Caesar cipher.

# NOTE: This is here just for educational purposes, you should not rely
# on the security of this cipher for sending messages. Vigenère ciphers are
# easily broken using simple techniques and modern hardware.
#
# Use aes.py to encrypt and decrypt messages with good security.

# python vigenere.py <message> <passphrase> --encrypt
# python vigenere.py <message> <passphrase> --decrypt

from utils import zip2


def encrypt_message(key, plaintext):
    return ''.join([chr((ord(c1) + ord(c2)) % 255) for c1, c2 in zip2(key, plaintext)])


def decrypt_message(key, ciphertext):
    return ''.join([chr((ord(c2) - ord(c1)) % 255) for c1, c2 in zip2(key, ciphertext)])


if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description=u'Encrypt an Decrypt messages with the historic Vigenère cipher.')
    parser.add_argument('text', help=u'The message to encrypt or decrypt depending on the operation being performed')
    parser.add_argument('passphrase', help=u'The passphrase with which to decrypt or encrypt the incoming text')
    parser.add_argument('--encrypt', '-e', action='store_true', help=u'Specify to encrypt the incoming message. Input text expected in ASCII format.')
    parser.add_argument('--decrypt', '-d', action='store_true', help=u'Specify to decrypt the incoming message. Input text expected in Hex format.')

    args = parser.parse_args()

    if args.encrypt:
        ct = encrypt_message(args.passphrase, args.text)
        print 'Your encrypted ciphertext is (in hex format):'
        print ct.encode('hex')

    elif args.decrypt:
        ct = args.text.decode('hex')
        print 'Your decrypted plaintext is:'
        print decrypt_message(args.passphrase, ct)

    else:
        print 'Please specify if you wish to --encrypt or --decrypt'
        sys.exit(1)
