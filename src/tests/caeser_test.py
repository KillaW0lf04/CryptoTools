from src.caesar import encrypt_message, decrypt_message


def test_integrity():
    plaintext = 'Test Text'

    # Ensure D(k, E(k, p)) == p
    for i in xrange(255):
        assert encrypt_message(i, decrypt_message(i, plaintext)) == plaintext
