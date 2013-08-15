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
  
 
  
