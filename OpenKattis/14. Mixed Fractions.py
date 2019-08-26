result = []

while True:
    numbers = input().split()
    numbers = [int(num) for num in numbers]
    if numbers[0] == 0 and numbers[1] == 0:
        break
    num1 = numbers[0] // numbers[1]
    num2 = numbers[0] % numbers[1]
    num3 = numbers[1]
    result.append(f"{num1} {num2} / {num3}")

for res in result:
    print(res)
