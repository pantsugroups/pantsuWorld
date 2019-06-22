x, y, z = 2, 2, 2
a = [[[0] * x for i in range(y)] * 1 for i in range(z)]
a[1][1][1] = 1
x, y, z = 0, 0, 0
for i in a:

    x += 1
    print(i)
    y = 0
    for j in i:
        y += 1
        z = 0
        for k in j:
            z += 1
            if k == 1:
                print(x, y, z)
print(a)