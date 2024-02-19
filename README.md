# Encryption and Decryption Tool

This tool provides functionalities for encryption and decryption using three different ciphers: Vigenère, Affine, and Caesar ciphers.

## How to Use

1. **Choose Cipher Type:** Enter the type of cipher you want to use (Vigenère, Affine, or Caesar).
2. **Choose Operation:** Select whether you want to encrypt or decrypt your text.
3. **Enter the Text:** Input the text you want to encrypt or decrypt.
4. **Provide Cipher Parameters:** Depending on the cipher type chosen, you'll need to provide additional parameters:
   - For Vigenère cipher, input the key.
   - For Affine cipher, input the values of 'a' and 'b'.
   - For Caesar cipher, input the shift value.
5. **View Result:** The tool will display the encrypted or decrypted text based on your input.

## Cipher Types

### Vigenère Cipher
The Vigenère cipher is a method of encrypting alphabetic text by using a keyword and rearranging the plaintext based on the letters of the keyword. It uses a simple form of polyalphabetic substitution.

### Affine Cipher
The Affine cipher is a type of monoalphabetic substitution cipher, where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.

### Caesar Cipher
The Caesar cipher is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Example Usage

Choose cipher type (vigenere/affine/caesar): vigenere
Choose operation (encrypt/decrypt): encrypt
Enter the text: Hello World
Enter the Vigenere key: key
Encrypted Text: Riijv Pyvnv
