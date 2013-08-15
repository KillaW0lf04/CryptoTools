from Crypto.Protocol.KDF import PBKDF1

from src.aes import encrypt_message, decrypt_message


def test_integrity():
    key = PBKDF1('Password1', '12345678', 16)
    plaintext = 'Test Text'

    # Ensure that D(k, E(k, p)) == p
    assert decrypt_message(key, encrypt_message(key, plaintext)) == plaintext
