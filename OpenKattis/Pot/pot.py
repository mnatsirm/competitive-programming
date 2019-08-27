number_test_case = int(input())
result = []

for i in range(number_test_case):
    addens = input()
    number = int(addens[:-1])
    pownumber = int(addens[-1])
    result.append(number ** pownumber)

print(sum(result))
