words = input().split()
check_words = list(set(words))

if len(words) == len(check_words):
    print('yes')
else:
    print('no')
