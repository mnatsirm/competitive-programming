date = input()

def isithalloween(date):
    if date == 'OCT 31' or date == 'DEC 25':
        return 'yup'
    return 'nope'


print(isithalloween(date))
