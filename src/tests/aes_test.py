from Crypto import Random

from src.aes import encrypt_message, decrypt_message


def test_integrity():
    plaintext = 'Test Text'
    key = Random.new().read(16)

    # Ensure that D(k, E(k, p)) == p
    assert decrypt_message(key, encrypt_message(key, plaintext)) == plaintext


def test_privacy():
    plaintext = 'Test Text'
    prng = Random.new()

    key1 = prng.read(16)
    key2 = prng.read(16)

    # Ensure decrypting with a different key does not reveal the plaintext
    assert decrypt_message(key1, encrypt_message(key2, plaintext)) != plaintext
