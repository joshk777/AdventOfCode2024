listA = []
listB = []

with open('input.txt', 'r') as file:

    for line in file:

        num1, num2 = map(int, line.split())

        listA.append(num1)
        listB.append(num2)

sorted_listA = sorted(listA)
sorted_listB = sorted(listB)

differences = [abs(num1 - num2) for num1, num2 in zip(sorted_listA, sorted_listB)]

totalDifference = sum(differences)

print("TotalDifference:", totalDifference)
