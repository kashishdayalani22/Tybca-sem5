print(chr(123))
plain_text = input("Enter the plain text : ")
key = int(input("enter the shift key : "))
str_list = list(plain_text.lower())
cipher = ''
for letter in str_list:
    if letter == " ":
        cipher += letter
    else:
        cipher += chr((ord(letter) - ord('a') + key) % 26 + ord('a'))
print(cipher)