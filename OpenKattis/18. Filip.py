numbers = input().split()
first_number, second_number = int(numbers[0][::-1]), int(numbers[1][::-1])

if first_number > second_number:
    print(first_number)
else:
    print(second_number)
