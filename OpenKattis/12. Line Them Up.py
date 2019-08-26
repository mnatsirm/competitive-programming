number_of_person = int(input())
name = []

for i in range(number_of_person):
    temp = input()
    name.append(temp)


def howsline(name):
    if sorted(name) == name:
        return 'INCREASING'
    elif sorted(name) == name[::-1]:
        return 'DECREASING'
    return 'NEITHER'


print(howsline(name))
