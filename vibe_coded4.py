def caesar_bruteforce_decrypt(ciphertext):
    """
    Attempts to decrypt the Caesar cipher by brute-forcing all possible shifts.
    Returns a list of tuples (shift, decrypted_text).
    """
    possibilities = []
    for shift in range(1, 26):  # 1 to 25 (0 would be the original text)
        decrypted = ""
        for char in ciphertext:
            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            elif char.islower():
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            else:
                decrypted += char
        possibilities.append((shift, decrypted))
    return possibilities

easter_egg = "Hkkg wp pda areh xnwjyd, dwdwdwdwdw"

if __name__ == "__main__":
    ciphertext = input("Enter Caesar cipher text to brute-force decrypt: ")
    results = caesar_bruteforce_decrypt(ciphertext)
    for shift, text in results:
        print(f"Shift {shift:2}: {text}")
