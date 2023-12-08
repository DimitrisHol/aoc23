import math

points = 0
matchingNumbers = {}
numberOfCopies = {}

with open("input/day04.txt", "r") as sourceFile : 

    for line in sourceFile : 
        line = line.strip()

        parts = line.split(" | ")

        cardNumber = parts[0].split(":")[0].replace(" ", "").split("Card")[1]
        winningNumbers = parts[0].split(":")[1].strip().split(" ")
        selectedNumbers = [x for x in parts[1].strip().split(" ") if x != ""]

        matches = 0
        for pickedNumber in selectedNumbers : 
            if pickedNumber in winningNumbers : 
                matches +=1

        # Part 1 
        if matches == 1 : 
            points += 1
            # print(1)
        elif matches > 1 :
            points += math.pow(2, matches-1)
            # print(math.pow(2, matches-1))

        # Part 2 
        matchingNumbers[int(cardNumber)] = matches
        numberOfCopies[int(cardNumber)] = 1 if matches > 0 else 0

        '''
        1 : 4
        2 : 2  + 1
        3 : 2  + 1
        4 : 1  + 1
        5 : 0  + 1
        6 : 0
        '''

print(f"Part 1: {int(points)}")

# Part 2 : 

# for i in range(1, len(matchingNumbers.keys()) + 1) : 
#     print(f"Card {i} | matching nums {matchingNumbers[i]} | copies {numberOfCopies[i]}")

for i in range(1, len(matchingNumbers.keys()) + 1) : 

    for j in range(i + 1, i + 1 + matchingNumbers[i]) : 
        numberOfCopies[j] += numberOfCopies[i]
        # print(f"From card {i} adding {numberOfCopies[i]} to card {j}, new total : {numberOfCopies[j]}")

# Results
# for i in range(1, len(matchingNumbers.keys()) + 1) : 
#     print(f"Card {i} | matching nums {matchingNumbers[i]} | copies {numberOfCopies[i]}")
        
# We are missing a count for the original copy of the card that didn't win

count = 0 
for value in matchingNumbers.values() : 
    if (value == 0) : 
        count += 1

print(f"Part 2: {sum(numberOfCopies.values()) + count}")

