def caesar_encrypt(text, shift):
    """
    Encrypts the input text using Caesar cipher with the given shift.
    Only letters are shifted; other characters are unchanged.
    """
    result = ""
    for char in text:
        if char.isupper():
            # Shift uppercase letters
            result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            # Shift lowercase letters
            result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # Non-alpha characters stay the same
            result += char
    return result

huh = "something is behind the...oh wait not suppose to say that here"

if __name__ == "__main__":
    text = input("Enter text to encrypt: ")
    shift = int(input("Enter shift (integer): "))
    encrypted = caesar_encrypt(text, shift)
    print("Encrypted text:", encrypted)
