CryptoTools
===========

A set crypto tools written in Python 2.7 which provide means of encrypting and decrypting data using technologies such as AES and RSA.

Requires the latest [PyCrypto](https://www.dlitz.net/software/pycrypto/) package to work.

The following tools are provided for your use:

aes.py
------

Encrypt and decrypt messages using the Advanced Encryption Standard. The tool makes use of a Key Derivation function to generate
an appropriate key from a given passphrase. Currently, only CFB (Cipher FeedBack) mode for AES is supported.

Encrypting can easily be done as follows:

```
python aes.py "Attack at Dawn" "Password1" --encrypt
# Your encrypted ciphertext is (in hex format):
# 072d9611db8bffa2a135fd24a12146a00de6948a7e260579a3bc46bea184
```
  
Decrypting can be performed using a similar step:

```
python aes.py 072d9611db8bffa2a135fd24a12146a00de6948a7e260579a3bc46bea184 "Password1" --decrypt
# Your decrypted plaintext is:
# Attack at Dawn
```
  
**Optional Arguments**
  
By default, a key size of 16 bytes is generated for AES-128. However, you may use the --key-size switch to specify between 16, 24 or 32 bytes.

```
python aes.py "Attack at Dawn" "Password1" --decrypt --key-size 32
```
  
The salt used for the generation of the key from the input password can be changed using the --salt switch. By Default, this would be set to '12345678'.

caesar.py
---------

Encrypt and decrypt messages using the historical Caesar cipher. The cipher is only included for educational purposes and should not be relied on
for transmitting messages securely. Messages encrypted with this cipher are *very* easily broken using frequency analysis. Apart from this, the
key space of this cipher is only 255 keys in size, meaning that all possible combinations can be brute forced by a computer in a matter of milliseconds.

Having said that, here is how to use caesar.py

Encrypting with the caesar cipher can be performed as follows:

```
python caesar.py "veni vidi vici" 14 --encrypt
# Your encrypted text is (in hex format):
# 84737c772e847772772e84777177
```

The output is kept in hex format to prevent the command line from printing invalid characters, which may result in corrupting your text when decrypting.

Decrypting can be then be performed as follows:

```
python caesar.py 84737c772e847772772e84777177 14 --decrypt
# Your decrypted text is:
# veni vidi vici
```

vigenere.py
-----------

Encrypt and decrypt messages with another historical cipher called the Vigenère cipher. This cipher is often thought to be the natural
evolution of the caesar cipher used during the Renaissance. Once again, this cipher is only included here for educational purposes
and should not be used to transmit messages securely. Vigenère ciphers can be broken using simple techniques (given enough data). Having
said that, it is much more secure than a caesar cipher.

Encrypting with the Vigenère cipher can be performed as follows:

```
python vigenere.py "La cifra del. Sig. Giovan Battista Bellaso" "Password1" --encrypt
# Your encrypted ciphertext is (in hex format):
# 9cc293d6e0d5e4c551b4c6dfa197c2dbcb5f70a8dce2edd0e08473b1d5e7dceae3d38473b5cddfd4eade
```

Decrypting can then be performed as follows:

```
python vigenere.py 9cc293d6e0d5e4c551b4c6dfa197c2dbcb5f70a8dce2edd0e08473b1d5e7dceae3d38473b5cddfd4eade "Password1" --decrypt
Your decrypted plaintext is:
La cifra del. Sig. Giovan Battista Bellaso
```
