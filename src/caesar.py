__author__ = 'Michael Aquilina'

# Encrypt and Decrypt messages using a very simple Caesar cipher
# NOTE: This is here just for educational purposes, you should not rely
# on the security of this cipher for sending messages. Caeser ciphers are
# very easily broken through frequency analysis.
#
# Use aes.py to encrypt and decrypt messages with good security.

# python caesar.py <message> <number> --encrypt
# python caesar.py <message> <number> --decrypt

# The <number> specified can be thought of as the key for this cipher


def encrypt_message(key, plaintext):
    return ''.join([chr((key + ord(c)) % 255) for c in plaintext])


def decrypt_message(key, ciphertext):
    return ''.join([chr((ord(c) - key) % 255) for c in ciphertext])

if __name__ == '__main__':
    import argparse
    import sys

    parser = argparse.ArgumentParser(description='Encrypt and Decrypt messages using a very simple Caesar cipher')
    parser.add_argument('text', help='The text to encrypt or decrypt depending on the operation being performed.')
    parser.add_argument('key', type=int, help='The key with which the encrypt or decrypt the incoming text. Integer value expected')
    parser.add_argument('--encrypt', '-e', action='store_true', help='Specify to encrypt the incoming message. Input text expected in ASCII format.')
    parser.add_argument('--decrypt', '-d', action='store_true', help='Specify to decrypt the incoming message. Input text expected in Hex format.')

    args = parser.parse_args()

    if args.encrypt:
        ct = encrypt_message(args.key, args.text)

        # Use hex encoding to prevent command line from printing wrong characters
        print 'Your encrypted text is (in hex format):'
        print ct.encode('hex')

    elif args.decrypt:
        ct = args.text.decode('hex')

        print 'Your decrypted text is:'
        print decrypt_message(args.key, ct)
    else:
        print 'Please specify if you wish to --encrypt or --decrypt'
        sys.exit(1)
