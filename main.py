def encrypt(text, shift):
    result=""
    for char in text:
      if char.isalpha():
         ascii_offset= ord('a') if char.islower() else ord('A')
         shifted= (ord(char)- ascii_offset + shift) % 26 + ascii_offset
         result += chr(shifted)
      else:
           result += char
    return result
user_message = input("Enter the message you want to encrypt:")
user_shift = int(input("Enter your secret shift number:"))

encrypted_message = encrypt(user_message, user_shift)
print(f"Encrypted message: {encrypted_message}")
