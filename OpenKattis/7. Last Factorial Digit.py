"""
1 1
2 2
3 6
4 4
5 0
6 0
...

"""
number_test_case = int(input())
numbers = []

for i in range(number_test_case):
    temp = int(input())
    numbers.append(temp)

for number in numbers:
    if number == 1:
        result = 1
    elif number == 2:
        result = 2
    elif number == 3:
        result = 6
    elif number == 4:
        result = 4
    else:
        result = 0
    
    print(result)
