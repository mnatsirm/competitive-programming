number_test_case = int(input())
results = []

for i in range(number_test_case):
    temp = input().split()
    temp = [int(num) for num in temp]
    N = temp[1]

    sum_first_N_positive = int(N * (N + 1) / 2)
    sum_first_N_odd = N ** 2
    sum_first_N_even = N * (N + 1)
    result = f"{i+1} {sum_first_N_positive} {sum_first_N_odd} {sum_first_N_even}"
    results.append(result)

for result in results:
    print(result)
