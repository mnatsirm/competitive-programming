number_test_case = int(input())

results = []

def whichoneisprofitable(revenue_not_adv, revenue_adv):
    if revenue_not_adv > revenue_adv:
        return 'do not advertise'
    elif revenue_not_adv == revenue_adv:
        return 'does not matter'
    return 'advertise'

for i in range(number_test_case):
    values = input().split()
    values = [int(val) for val in values]
    revenue_not_adv = values[0]
    revenue_adv = values[1] - values[2]
    results.append(whichoneisprofitable(revenue_not_adv, revenue_adv))


for result in results:
    print(result)
