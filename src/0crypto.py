def encrypt(password):
    crypt_password = ''
    for i in password:
        character = ord(i)
        character += 7
        crypt_password += chr(character)
    return crypt_password


def decrypt(password):
    crypt_password = ''
    for i in password:
        character = ord(i)
        character -= 7
        crypt_password += chr(character)
    return crypt_password
