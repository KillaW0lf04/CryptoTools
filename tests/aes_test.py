from Crypto.Protocol.KDF import PBKDF1
from aes import encode_message, decode_message


def test_integrity():
    key = PBKDF1('Password1', '12345678', 16)
    plaintext = 'Test Text'

    # Ensure that E(k, D(k, p)) == p
    assert decode_message(key, encode_message(key, plaintext)) == plaintext
