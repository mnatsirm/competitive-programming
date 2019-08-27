number = int(input())
its_binary = "{:b}".format(number)

new_number = its_binary[::-1]
print(int(new_number, 2))
