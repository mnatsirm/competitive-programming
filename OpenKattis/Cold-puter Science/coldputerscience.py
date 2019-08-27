num_case = int(input())
temperature = input().split()

temperature = [int(num) for num in temperature if int(num) < 0]
print(len(temperature))
