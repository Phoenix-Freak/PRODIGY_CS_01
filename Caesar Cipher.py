def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            # Determine if the character is uppercase or lowercase
            offset = 65 if char.isupper() else 97
            # Encrypt the character
            encrypted_char = chr((ord(char) - offset + shift) % 26 + offset)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain the same
    return encrypted_text


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decryption is the same as encryption with a negative shift


def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        choice = input("Choose an option: (1) Encrypt (2) Decrypt (3) Exit: ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)

        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
