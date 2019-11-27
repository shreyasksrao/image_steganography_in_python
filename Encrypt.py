def encrypt(text, key):
    encrypted_text = ""
    text = text.upper()
    for letters in text:
        ascii_of_letter = ord(letters)
        if (ord("A") > ascii_of_letter) or (ascii_of_letter > ord("Z")):
            encrypted_text += letters
        else:
            key_value = ascii_of_letter + key
            if not((ord("A")) < key_value < ord("Z")):
                key_value = ord("A") + ((key_value - ord("A")) % 26)
            encrypted_text += str(chr(key_value))
    return encrypted_text


def encrypt_multilevel(text, level, keys):
    encrypted_text = [text]
    for i in range(level):
        encrypt_level = encrypt(encrypted_text[i], keys[i])
        encrypted_text.append(encrypt_level)
    return encrypted_text[-1]


if __name__ == "__main()__":
    print("Enter the text to be encrypt :")
    text_ip = input()
    encrypted = encrypt_multilevel(text_ip, 3, [2, 5, 4])
    print(encrypted)
    decrypt = encrypt_multilevel(encrypted, 3, [-2, -5, -4])
    print(decrypt)
    