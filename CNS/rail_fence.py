import numpy as np

plain_text = input("Enter the plain text : ").upper().replace(' ', '')
key = int(input("Enter your key : "))
cipher = ''

grid = np.full((key, len(plain_text)), '#')
j = 0
x = 1
for i in range(len(plain_text)):
    grid[j] [i] = plain_text[i]
    j += x
    if j == key - 1 or j == 0:
        x *= (-1)

for i in range(key):
    for j in range(len(plain_text)):
        if grid[i][j] != '#':
            cipher += grid[i][j]
print(grid)
print(cipher)

