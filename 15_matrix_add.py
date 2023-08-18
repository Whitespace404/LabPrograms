a = [
        [1,2,3],
        [3,2,1],
        [4,1,0]
    ]

b = [
        [2,4,1],
        [1,3,2],
        [1,0,2]
    ]

result = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

for i in range(len(a)):
    for j in range(len(b[0])):
        result[i][j] = a[i][j] + b[i][j]

for list in result:
    print(list)
