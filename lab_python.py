def main():
    leftRightSideRectangle = ""
    ringString1 = "-"
    ringString2 = "|"
    coreString1 = "/"
    coreString2 = "\\"
    newLine = "\n"
    space = " "
    alignmentForUpDown = ""
    counter = 0
    rings = int(input("Enter the number of rings you would like "))

    #Base Cases
    if rings <= 0:
        print("The number of rings has to be greater than zero")
        exit(-1)

    coreSize = int(input("Enter the number of cores you would like "))

    if coreSize < 0:
        print("The core size cannot be negative")
        exit(-1)

    while rings != 0 and coreSize != 0:
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
        while counter != 0:
            hyphin = ringString1 * coreSize
            print(f'{alignmentForUpDown}{hyphin}')
            counter -= 1

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
        while counter != 0:
            hyphin = ringString1 * coreSize
            print(f'{alignmentForUpDown}{hyphin}')
            counter -= 1
        break



    #print(f"Rings: {rings}")
    #print(f"Core Size: {coreSize}")






if __name__ == '__main__':
    main()
