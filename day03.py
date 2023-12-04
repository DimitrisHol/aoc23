from collections import defaultdict

specialCharacters = set(['#', '%', '/', '-', '&', '@', '$', '*', '+', '='])
totalSum = 0 

with open("input/day03.txt", "r") as sourceFile : 

    twodimensions = []

    for line in sourceFile : 
        line = line.strip()

        newRow = [x for x in line]
        # You don't need the end of the line logic
        # newRow.append(".") # Elves hate this simple trick. 
        twodimensions.append(newRow)

# ['4', '6', '7', '.', '.', '1', '1', '4', '.', '.']
# ['.', '.', '.', '*', '.', '.', '.', '.', '.', '.']
# ['.', '.', '3', '5', '.', '.', '6', '3', '3', '.']

# We want to create a map to retrieve the number given the coordinates
# x,y = 0,0 [467, False, groupA]
# x,y = 0,1 [467, False, groupA]
# x,y = 0,2 [467, False, groupA]
# x,y = 0,5 [114, False, groupB]
# x,y = 0,6 [114, False, groupB]
# x,y = 0,7 [114, False, groupB]

# boolean is the visit, to avoid summing twice

searchMap = defaultdict(lambda:[0, False, 0])

globalIterator = 1

for i in range(len(twodimensions)) : 
    numberLength = 0 

    # iterate through the row to find the start and the end of the number
    for j in range(len(twodimensions[i])) : 

        if twodimensions[i][j].isnumeric() : 
            numberLength += 1
        else : 
            if numberLength > 0 : 
                coords = [f"{i},{x}" for x in range(j-1, j - numberLength -1, -1)]
                number = int("".join(twodimensions[i][j-numberLength:j]))

                # print(coords, number)
                for coordinate in coords : 
                    searchMap[coordinate][0] = number
                    searchMap[coordinate][2] = globalIterator

                globalIterator += 1
                numberLength = 0

        # end of the line
        if twodimensions[i][j].isnumeric() and j == len(twodimensions[i])-1: 

            coords = [f"{i},{x}" for x in range(j-1, j - numberLength -1, -1)]
            number = int("".join(twodimensions[i][j-numberLength+1:j+1]))

            # print(coords, number)
            for coordinate in coords : 
                searchMap[coordinate][0] = number
                searchMap[coordinate][2] = globalIterator

            globalIterator += 1
            numberLength = 0

for i in range(1, len(twodimensions)-1) : 
    for j in range(1, len(twodimensions[i])-1) : 

        if twodimensions[i][j] in specialCharacters : 

            # Loop through adjacent tiles (distance = 1) : 
            for k in [i-1, i , i +1] : 
                for n in [j -1, j, j+1] : 

                    if twodimensions[k][n].isnumeric() : 
                        coordinates = f"{k},{n}"

                        # Retrieve the visit value
                        if not searchMap[coordinates][1] : 

                            # Add to the total, using the number
                            totalSum += searchMap[coordinates][0]

                            # Set the visit to true
                            searchMap[coordinates][1] = True
                            
                            # fetch out the group
                            groupingIterator = searchMap[coordinates][2]
                                
                            # Set all same group visits to true

                            for value in searchMap.values() : 
                                if value[2] == groupingIterator : 
                                    value[1] = True 
print(f"Part 1: {totalSum}")
