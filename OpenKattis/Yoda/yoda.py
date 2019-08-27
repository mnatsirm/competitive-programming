first_number = input()
second_number = input()

selisih = abs(len(first_number) - len(second_number))
if len(first_number) > len(second_number):
    second_number = '0' * selisih + second_number
elif len(first_number) < len(second_number):
    first_number = '0' * selisih + first_number

first_result = ''
second_result = ''

for i in range(len(first_number)):
    if first_number[i] > second_number[i]:
        first_result += first_number[i]
    elif first_number[i] < second_number[i]:
        second_result += second_number[i]
    else:
        first_result += first_number[i]
        second_result += second_number[i]

if len(first_result) == 0:
    print('YODA')
else:
    print(int(first_result))

if len(second_result) == 0:
    print('YODA')
else:
    print(int(second_result))
