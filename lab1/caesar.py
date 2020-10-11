def encrypt_caesar(plaintext):
    """
    Encrypts a plaintext using a Caesar cipher

    >>> encrypt_caesar("!abc123")
    '!def123'
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for c in plaintext:
        if (ord(c) <= 64) or (91 <= ord(c) <= 96) or (123 <= ord(c)):
            ciphertext += chr(ord(c))
        elif (97 <= ord(c) + 3 <= 122) or (65 <= ord(c) + 3 <= 90):
            ciphertext += chr(ord(c) + 3)
        else:
            ciphertext += chr(ord(c) + 3 - 26)
    return ciphertext


def decrypt_caesar(ciphertext):
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("!def123")
    '!abc123'
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for c in ciphertext:
        if (ord(c) <= 64) or (91 <= ord(c) <= 96) or (123 <= ord(c)):
            plaintext += chr(ord(c))
        elif (97 <= ord(c) - 3 <= 122) or (65 <= ord(c) - 3 <= 90):
            plaintext += chr(ord(c) - 3)
        else:
            plaintext += chr(ord(c) - 3 + 26)
    return plaintext
