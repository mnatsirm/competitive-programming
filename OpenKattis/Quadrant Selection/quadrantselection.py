x = int(input())
y = int(input())

def quadrant_selection(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    return 4

result = quadrant_selection(x, y)
print(result)
