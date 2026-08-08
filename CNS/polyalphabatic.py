plain_text = input("Enter the plain text : ")
key = input("enter the shift key (string) : ")
str_list = list(plain_text.lower())
cipher = ''
i = 0
for letter in str_list:
    if letter == " ":
        cipher += letter
    else:
        cipher += chr((ord(letter) - ord('a') + (ord(key[ i % len(key)]) - ord('a'))) % 26 + ord('a'))
        i += 1

print(cipher)