number_test_case = int(input())
results = []

for i in range(number_test_case):
    temp = input().split()
    temp = [int(num) for num in temp]
    xs, ys = temp[1::2] + [temp[1]], temp[2::2] + [temp[2]]

    xs1, ys1 = xs[0:-1], ys[1:]
    xs2, ys2 = xs[1:], ys[0:-1]
    totalx, totaly = 0, 0
    for i in range(len(xs1)):
        totalx += xs1[i] * ys1[i]
        totaly += xs2[i] * ys2[i]
    result = 0.5 * (totalx - totaly)
    results.append(result)

for result in results:
    print(result)
