from Crypto.Protocol.KDF import PBKDF1
from Crypto.Cipher import AES
from Crypto import Random

from aes import encode_message, decode_message


# Test to check if pycrypto is working well
def test_pycrypto_aes():
    prng = Random.new()
    key = prng.read(16)
    iv = prng.read(AES.block_size)

    assert len(iv) == 16
    assert len(key) == 16

    cipher = AES.new(key, AES.MODE_CFB, iv)

    # Assert result is a multiple of 16
    assert len(cipher.encrypt('Test Text')) % 16 == 0


def test_integrity():
    key = PBKDF1('Password1', '12345678', 16)
    plaintext = 'Test Text'

    # Ensure that E(k, D(k, p)) == p
    assert decode_message(key, encode_message(key, plaintext)) == plaintext
