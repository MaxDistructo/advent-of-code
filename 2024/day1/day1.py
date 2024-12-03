with open("input.txt", "r") as f:
    lines = f.readlines()
    
list1 = []
list2 = []

for line in lines:
    list1.append(int(line.split("   ")[0]))
    list2.append(int(line.split("   ")[1]))

list1.sort()
list2.sort()

distance_between = 0

for i in range(len(list1)):
    val1 = list1[i]
    val2 = list2[i]
    distance_between += abs(val1-val2)

print("Part 1 Answer: ", distance_between)

similarity_score = 0

for i in range(len(list1)):
    similarity_score += list1[i] * list2.count(list1[i])

print("Part 2 Answer: ", similarity_score)