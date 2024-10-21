with open('input.txt', 'r') as file:
    lines = file.readlines()
lines = [line for line in lines for _ in range(2)]
with open('output.txt', 'w') as file:
    file.writelines(lines)```
