number_test_case = int(input())
results = []

for i in range(number_test_case):
    number_cities = int(input())
    cities_visited = []
    for j in range(number_cities):
        temp = input()
        cities_visited.append(temp)

    results.append(len(set(cities_visited)))

for result in results:
    print(result)
