def main():
    while True:
        ringString1 = "-"
        ringString2 = "|"
        coreString1 = "/"
        coreString2 = "\\"
        space = " "
        backSpace = "\b"
        alignmentForUpDown = ""

        rings = int(input("Rings: "))

        # Base Cases
        if rings < 0:
            print("The number of rings has to be greater than zero")
            exit(-1)

        coreSize = int(input("Core Size: "))

        if coreSize < 0:
            print("The core size cannot be negative")
            exit(-1)

        if rings == 0 and coreSize == 0:
            break

        print('\n')
        horizontalSpace = coreSize * space
        verticalLines = ringString2 * rings

        # Alignment for upper rectangle
        spaceCounter = rings
        while spaceCounter != 0:
            alignmentForUpDown += " "
            spaceCounter -= 1

        counter = rings
        fowardSlash = coreString1
        backSlash = coreString2
        ringsCounter = 1
        backSpaceCounter = 0
        # Top part of rectangle
        while counter != 0:
            backSpace = backSpace * (backSpaceCounter + 1)
            hyphin = ringString1 * coreSize
            print(f'{alignmentForUpDown}{backSpace}{fowardSlash}{hyphin}{backSlash}')
            backSpace = '\b'
            backSpaceCounter += 1
            counter -= 1
            ringsCounter += 1
            fowardSlash = coreString1 * (ringsCounter)
            backSlash = coreString2 * (ringsCounter)

        # Print the empty core
        counter = coreSize
        while counter != 0:
            printCore = verticalLines + horizontalSpace + verticalLines
            print(printCore)
            counter -= 1

        # Bottom part of rectangle
        counter = rings
        backSpaceCounter = 0
        fowardSlash = coreString1 * (rings)
        backSlash = coreString2 * (rings)
        backSpace = '\b'
        space = ""
        while counter != 0:
            backSpace = backSpace * (backSpaceCounter + 1)
            hyphin = ringString1 * coreSize
            print(f'{backSpace}{space}{backSlash}{hyphin}{fowardSlash}')
            backSpace = '\b'
            space += " "
            backSpaceCounter += 1
            fowardSlash = coreString1 * (counter - 1)
            backSlash = coreString2 * (counter - 1)
            counter -= 1
        print('\n')


if __name__ == '__main__':
    main()
