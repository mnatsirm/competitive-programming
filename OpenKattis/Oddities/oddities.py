num_test_case = int(input())
number = []

for i in range(num_test_case):
    temp = int(input())
    number.append(temp)
    
for num in number:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
