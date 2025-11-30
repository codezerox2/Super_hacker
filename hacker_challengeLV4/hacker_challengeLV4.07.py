## XOR encryption function
def XOR_enc(plaintext, key):
    enc = ''

    for i in range(len(plaintext)):
        enc += chr(ord(plaintext[i]) ^ ord(key[i % len(key)]))
    return enc

plaintext = 'encrypted_string'
key = 'super_hacker'
encrypt = XOR_enc(plaintext, key)
print(encrypt.encode('utf-8'))