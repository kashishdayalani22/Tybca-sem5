plain_text = input("Enter the plain text : ")
key = int(input("enter the shift key : "))
cipher = plain_text[key:] + plain_text[:key]
print(cipher)