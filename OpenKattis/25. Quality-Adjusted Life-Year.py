number_test_case = int(input())
result = []
for i in range(number_test_case):
    temp = input().split()
    quality_of_life = float(temp[0])
    number_of_years_period = float(temp[1])
    result.append(quality_of_life * number_of_years_period)

print(sum(result))
