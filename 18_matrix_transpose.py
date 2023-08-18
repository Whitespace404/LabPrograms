a = [
        [1,2,3],
        [3,2,1]
    ]

result = [
        [0,0],
        [0,0],
        [0,0]
]

for i in range(len(a)):
    for j in range(len(a[0])):
        result[j][i] = a[i][j]

for line in result:
    print(line)
