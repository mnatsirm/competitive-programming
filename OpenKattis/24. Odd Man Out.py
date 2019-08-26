number_test_case = int(input())
results = []

for i in range(number_test_case):
    number_of_quests = int(input())
    number_invitation = input().split()
    number_invitation = [int(num) for num in number_invitation]
    
    result = 2 * sum(list(set(number_invitation))) - sum(number_invitation)
    results.append(result)
    
for i in range(len(results)):
    print(f"Case #{i+1}: {results[i]}")
