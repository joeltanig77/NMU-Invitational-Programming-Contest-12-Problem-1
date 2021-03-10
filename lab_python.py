def main():
    leftRightSideRectangle = ""
    ringString1 = "-"
    ringString2 = "|"
    coreString1 = "/"
    coreString2 = "\\"
    newLine = "\n"
    space = " "
    backSpace = "\b"
    alignmentForUpDown = ""

    rings = int(input("Enter the number of rings you would like "))

    #Base Cases
    if rings < 0:
        print("The number of rings has to be greater than zero")
        exit(-1)

    coreSize = int(input("Enter the number of cores you would like "))

    if coreSize < 0:
        print("The core size cannot be negative")
        exit(-1)

    while True:
        print(f"Rings: {rings}")
        print(f"Core Size: {coreSize}")
        horizontalSpace = coreSize*space
        verticalLines = ringString2*rings


        #Alignment for upper rectangle
        if coreSize % 2 == 0:
            spaceCounter = coreSize/2
            while spaceCounter != 0:
                alignmentForUpDown += " "
                spaceCounter -= 1
        else:
            spaceCounter = rings
            while spaceCounter != 0:
                alignmentForUpDown += " "
                spaceCounter -= 1

        counter = rings
        fowardSlash = coreString1
        backSlash = coreString2
        ringsCounter = 1
        backSpaceCounter = 0
        #if its a even core.
        while counter != 0:
            if coreSize % 2 == 0:
                backSpace = backSpace*(backSpaceCounter) #Delete +1 for odd
            #backSpaceTESTEVEN = backSpace*(backSpaceCounter)
            else:
                backSpace = backSpace * (backSpaceCounter+1)
            hyphin = ringString1 * coreSize

            print(f'{alignmentForUpDown}{backSpace}{fowardSlash}{hyphin}{backSlash}')
            backSpace = '\b'

            backSpaceCounter += 1
            counter -= 1
            ringsCounter += 1
            fowardSlash = coreString1 * (ringsCounter)
            backSlash = coreString2 * (ringsCounter)

        counter = coreSize
        while counter != 0:
            leftRightSideRectangle = verticalLines + horizontalSpace + verticalLines
            print(leftRightSideRectangle)
            counter -= 1

        #Alignment for lower rectangle
        alignmentForUpDown = ""
        if coreSize % 2 == 0:
            spaceCounter = coreSize/2
            while spaceCounter != 0:
                alignmentForUpDown += " "
                spaceCounter -= 1
        else:
            spaceCounter = rings
            while spaceCounter != 0:
                alignmentForUpDown += " "
                spaceCounter -= 1

        counter = rings
        ringsCounter = rings
        fowardSlash = coreString1 * (ringsCounter)
        backSlash = coreString2 * (ringsCounter)
        ringsCounter = rings
        while counter != 0:
            hyphin = ringString1 * coreSize
            print(f'{alignmentForUpDown}{backSlash}{hyphin}{fowardSlash}')
            counter -= 1
            ringsCounter -= 1
            fowardSlash = coreString1 * ringsCounter
            backSlash = coreString2 * ringsCounter

        break



    #print(f"Rings: {rings}")
    #print(f"Core Size: {coreSize}")






if __name__ == '__main__':
    main()
