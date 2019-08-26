sentence = input()
white_space = 0
lowercase = 0
uppercase = 0
symbol = 0
total = len(sentence)

for ch in sentence:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch == '_':
        white_space += 1
    else:
        symbol += 1

print(white_space / total)
print(lowercase / total)
print(uppercase / total)
print(symbol / total)
