from typing import ForwardRef


f = open('input.txt', 'r')

values = f.read().split('\n')

hor = 0
depth = 0

for i in values:
    tmp = i.split()
    if tmp[0] == "forward":
        hor += int(tmp[1])
    elif tmp[0] == "up":
        depth -= int(tmp[1])
    else:
        depth += int(tmp[1])

print(depth, hor, depth * hor)