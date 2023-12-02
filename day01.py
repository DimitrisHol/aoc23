from collections import defaultdict

def calculateValue(line) : 

    for character in line: 
        if character.isnumeric() : 
            firstCharacter = character
            break

    for reverseCharacter in line[::-1] :
        if reverseCharacter.isnumeric() :
            lastCharacter = reverseCharacter
            break

    return int(firstCharacter + lastCharacter)


def part1() : 
    with open("input/day01.txt", "r") as sourceFile : 

        totalSum = 0
        for line in sourceFile : 
            line = line.strip()
            totalSum += calculateValue(line)

    print(totalSum)

def part2 () : 

    digitsMap = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine" : "9"}
    totalSum = 0

    with open("input/day01.txt", "r") as sourceFile : 

        for line in sourceFile : 
            line = line.strip()

            hits = defaultdict(list)

            # Figure out the hits for numbers : 
            for i in range(len(line)) :

                if line[i].isnumeric() : 
                    hits[line[i]].append(i)

            # Now for the alphanumerics : 
            for digit in digitsMap.keys() : 

                copyLine = line

                foundIndex = copyLine.find(digit)

                while (foundIndex != -1) : 
                    
                    # Figure the number
                    actualNumber = digitsMap[digit]
                    
                    # Add the index of the hit
                    hits[actualNumber].append(foundIndex)

                    # Remove the occurence from the line : 
                    copyLine = copyLine.replace(digit, " " * len(digit), 1)
                    
                    # Find the next occurence!
                    foundIndex = copyLine.find(digit)
            
            maximum = -1
            minimum = 2000
            minNumber = ""
            maxNumber = ""

            for key, occurences in hits.items() : 

                if min(occurences) < minimum : 
                    minimum = min(occurences)
                    minNumber = key

                if max(occurences) > maximum : 
                    maximum = max(occurences)
                    maxNumber = key

            totalSum += (int(minNumber + maxNumber))

    print(totalSum)

part1()
part2()


