plain_text = input("Enter the plain text : ")
key = input("enter the shift key (string) : ")
str_list = list(plain_text.lower())
cipher = ''
i = 0
for letter in str_list:
    if letter == " ":
        cipher += letter
    else:
        a = ord(letter) - ord('a')

        b = (ord(key[i % len(key)]) - ord('a'))

        cipher += chr((a + b) % 26 + ord('a'))

        i += 1

print(cipher)
