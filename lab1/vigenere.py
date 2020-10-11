def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    letters_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
    a = 26

    while len(keyword) < len(plaintext):
        keyword += keyword

    ciphertext = ""

    for i in range(len(plaintext)):
        pc = ord(plaintext[i])

        if keyword[i] in letters_uppercase:
            N = ord(keyword[i]) - ord("A")
        elif keyword[i] in letters_lowercase:
            N = ord(keyword[i]) - ord("a")

        if (97 <= pc + N <= 122) and pc > 96 and pc < 123 \
                or (65 <= pc + N <= 90) and pc > 64 and pc < 91:
            ciphertext += chr(pc + N)
        else:
            ciphertext += chr(pc + N - a)

    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    letters_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
    a = 26

    while len(keyword) < len(ciphertext):
        keyword += keyword

    plaintext = ""

    for i in range(len(ciphertext)):
        ct = ord(ciphertext[i])

        if keyword[i] in letters_uppercase:
            K = ord(keyword[i]) - ord("A")
        elif keyword[i] in letters_lowercase:
            K = ord(keyword[i]) - ord("a")

        if (97 <= ct - K <= 122) and ct > 96 and ct < 123 \
                or (65 <= ct - K <= 90) and ct > 64 and ct < 91:
            plaintext += chr(ct - K)
        else:
            plaintext += chr(ct - K + a)
    return plaintext
