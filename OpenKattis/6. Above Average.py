number_test_case = int(input())
rate_above = []

def above_average(values):
    mean = sum(values) / number_student
    sucess = 0
    for num in values:
        if num > mean:
            sucess += 1
    
    return sucess

for num in range(number_test_case):
    number = input().split()
    number = [int(num) for num in number]
    
    number_student = number[0]
    values = number[1:]

    rate_above.append(above_average(values) / number_student * 100)
    
for rate in rate_above:
    print(f"{format(rate, '.3f')}%")    
