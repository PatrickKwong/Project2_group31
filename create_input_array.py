V = [1, 5, 10, 25, 50]
A = []
for num in range(2010, 2201):
    A.append(num)

with open("question3.txt", "w+") as f:
    for num in A:
        f.write("{0}\n{1}\n".format(V, num))

V1 = [1, 2, 6, 12, 24, 48, 60]
V2 = [1, 6, 13, 37, 150]
A = []
for num in range(2000, 2201):
    A.append(num)

with open("question4.txt", "w+") as f:
    for num in A:
        f.write("{0}\n{1}\n".format(V1, num))
        f.write("{0}\n{1}\n".format(V2, num))

V = []
V.append(1)
for num in range(2, 31, 2):
    V.append(num)

with open("question5.txt", "w+") as f:
    for num in A:
        f.write("{0}\n{1}\n".format(V, num))

V = [1, 5, 10, 25, 50, 100, 500, 1000, 2000]
V_array = []
for num in range(len(V) - 1):
    V_array.append([])
    V_array[num] = V[:num+1]

with open("question7.txt", "w+") as f:
    for num in A:
        for V in V_array:
            f.write("{0}\n{1}\n".format(V, num))

