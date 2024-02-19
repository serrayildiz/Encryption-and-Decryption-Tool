def mod_inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def vigenere_cipher(text, key, decrypt=False):
    key = key.lower()
    result = ''
    key_index = 0

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_index = ord(char) - ord('a')
            key_char = key[key_index % len(key)]
            key_index += 1
            key_index_char = ord(key_char) - ord('a')
            
            if decrypt:
                decrypted_index = (char_index - key_index_char) % 26
            else:
                decrypted_index = (char_index + key_index_char) % 26
                
            decrypted_char = chr(decrypted_index + ord('a'))
            result += decrypted_char.upper() if is_upper else decrypted_char
        else:
            result += char

    return result

def affine_cipher(text, a, b, decrypt=False):
    result = ''
    a_inv = mod_inverse(a, 26)

    if a_inv is None:
        print("Invalid 'a' value. Modular inverse does not exist.")
        return

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_index = ord(char) - ord('a')

            if decrypt:
                decrypted_index = (a_inv * (char_index - b)) % 26
            else:
                decrypted_index = (a * char_index + b) % 26

            decrypted_char = chr(decrypted_index + ord('a'))
            result += decrypted_char.upper() if is_upper else decrypted_char
        else:
            result += char

    return result

def caesar_cipher(text, shift, decrypt=False):
    result = ''

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()
            char_index = ord(char) - ord('a')

            if decrypt:
                decrypted_index = (char_index - shift) % 26
            else:
                decrypted_index = (char_index + shift) % 26

            decrypted_char = chr(decrypted_index + ord('a'))
            result += decrypted_char.upper() if is_upper else decrypted_char
        else:
            result += char

    return result

def main():
    cipher_type = input("Choose cipher type (vigenere/affine/caesar): ").lower()

    if cipher_type not in ['vigenere', 'affine', 'caesar']:
        print("Invalid cipher type. Please choose vigenere, affine, or caesar.")
        return

    operation = input("Choose operation (encrypt/decrypt): ").lower()

    if operation not in ['encrypt', 'decrypt']:
        print("Invalid operation. Please choose encrypt or decrypt.")
        return

    input_text = input("Enter the text: ")

    if cipher_type == 'vigenere':
        key = input("Enter the Vigenere key: ")
        if operation == 'encrypt':
            result = vigenere_cipher(input_text, key)
        else:
            result = vigenere_cipher(input_text, key, decrypt=True)

    elif cipher_type == 'affine':
        a = int(input("Enter the value of 'a' in the affine cipher: "))
        b = int(input("Enter the value of 'b' in the affine cipher: "))
        if operation == 'encrypt':
            result = affine_cipher(input_text, a, b)
        else:
            result = affine_cipher(input_text, a, b, decrypt=True)

    elif cipher_type == 'caesar':
        shift = int(input("Enter the Caesar shift value: "))
        if operation == 'encrypt':
            result = caesar_cipher(input_text, shift)
        else:
            result = caesar_cipher(input_text, shift, decrypt=True)

    print(f"{operation.capitalize()}ed Text: {result}")

if __name__ == "__main__":
    main()
