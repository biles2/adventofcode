f = open("input.txt", 'r')

values = f.read().split('\n')

tmp0 = 0
tmp1 = 0

gamma = []
epsilon = []

for i in range(len(values[0])):
    for f in range(len(values)):
        if values[f][i] == '0':
            tmp0 += 1
        else:
            tmp1 += 1

    if (tmp0 > tmp1):
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')
    tmp0 = 0
    tmp1 = 0

gammaInt = int("".join(gamma), 2)
epsilonInt = int("".join(epsilon), 2)

print(gammaInt * epsilonInt)