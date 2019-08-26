# number_test_case = int(input())
results = []

while True:
    number_pair = int(input())
    if number_pair == -1:
        break
    
    speed, time = [], []
    for num in range(number_pair):
        temp = input().split()
        speed.append(int(temp[0]))
        time.append(int(temp[1]))
    
    total_miles = 0
    if number_pair > 1:
        speed2, time2 = speed[1:], time[0:-1]
        for i in range(number_pair):
            total_miles += speed[i] * time[i]
        for i in range(len(speed2)):
            total_miles -= speed2[i] * time2[i]
        results.append(total_miles)
    else:
        results.append(speed[0] * time[0])

for result in results:
    print(f"{result} miles")
