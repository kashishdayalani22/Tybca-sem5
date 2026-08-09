plain_text = input("Enter the plain text : ").lower().replace(' ', '')
key = input("Enter your key : ").lower().replace(' ', '')
cipher = ''
matrix = [[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i/j', 'k', 'l', 'm',
            'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
i, j = 0, 0
for char in key:
    if j > 4:
        j = 0
        i = i + 1
    if char == 'i' or char == 'j':
        matrix[i][j] = 'i/j'
        alphabet.remove('i/j')
        j = j + 1
        continue

    matrix[i][j] = char
    j = j +1
    alphabet.remove(char)

for char in alphabet:
    if j > 4:
        j = 0
        i = i + 1
    matrix[i][j] = char
    j = j + 1

for row in matrix:
    print(row)

if len(plain_text) % 2 != 0:
    plain_text += 'x'

for i in range(0, len(plain_text), 2):
    for a in range(5):
        for b in range(5):
            if matrix[a][b] == plain_text[i]:
                x = [a, b]
            if matrix[a][b] == plain_text[i + 1]:
                y = [a, b]
    if x[0] == y[0]:
        cipher += matrix[x[0]] [(x[1] + 1) % 5] + matrix[y[0]] [(y[1] + 1) % 5]

    elif x[1] == y[1]:
        cipher += matrix[(x[0] + 1) % 5] [x[1]] + matrix[(y[0] + 1) % 5] [y[1]]
    else:
        cipher += matrix[y[0]] [x[1]] + matrix[x[0]] [y[1]]

print(cipher)