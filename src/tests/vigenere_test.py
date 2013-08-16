from src.vigenere import encrypt_message, decrypt_message

def integrity_test():
    plaintext = 'Hello world! Test Text'
    key = 'Password1'

    # Ensure D(k, E(k, p)) == p
    assert decrypt_message(key, encrypt_message(key, plaintext))

def privacy_test():
    plaintext = 'Hello world! Test Text'
    key1 = 'Password1'
    key2 = 'WrongPass'

    # Ensure decrypting with the wrong key does not reveal the plaintext
    assert decrypt_message(key1, encrypt_message(key2, plaintext)) != plaintext
