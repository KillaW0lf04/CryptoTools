from Crypto.Protocol.KDF import PBKDF1
from Crypto.Cipher import AES
from Crypto import Random

from aes import encrypt_message, decrypt_message


def test_integrity():
    key = PBKDF1('Password1', '12345678', 16)
    plaintext = 'Test Text'

    # Ensure that E(k, D(k, p)) == p
    assert decrypt_message(key, encrypt_message(key, plaintext)) == plaintext
