my_number = []
for i in range(10):
    temp = int(input())
    my_number.append(temp)


result = []
for num in my_number:
    result.append(num % 42)

print(len(set(result)))
