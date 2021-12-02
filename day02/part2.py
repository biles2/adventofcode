from typing import ForwardRef


f = open('input2.txt', 'r')

values = f.read().split('\n')

hor = 0
depth = 0
aim = 0

for i in values:
    tmp = i.split()
    if tmp[0] == "forward":
        hor += int(tmp[1])
        depth += int(tmp[1]) * aim
    elif tmp[0] == "up":
        aim -= int(tmp[1])
    else:
        aim += int(tmp[1])

print(depth, hor, depth * hor)