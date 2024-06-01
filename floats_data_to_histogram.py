***
This python program will take in a text file named input and processes the data numerical data within the file. The data within the file contains lines floats seperated by 
commas (as a .csv file would). Each line contains equal number of floats. The data is processed to create two rows that can be used with a spreadsheet program like Excel.
This was part of a course lab exercise.
***


# The example in class produced the data that could be used to produce a
# histogram with increments of 10 degrees.
# Modify it to produce data for a histogram with 5 degree increments.

def preprocessFile(filename="input.txt"):
    try:
        ifs = open(filename)
    except:
        print(f"{filename} did NOT open!")
        return
    histoRanges = []
    for text in ifs:
        text = text.rstrip()
        text = text.replace(" ", "")
        #.split() returns type list
        numbers = text.split(",")
        for number in numbers:
            n = int(float(number))
            #n-->62, n//10-->6 n//5-->12
            histoRanges.append(n)
    ifs.close()
    scale = processHistoRangesScale(histoRanges)
    values = processHistoRangesValues(histoRanges)
    return scale, values

def processHistoRangesScale(histoRanges):
    findHighest = findLowestHighest(histoRanges)[0]
    findLowest = findLowestHighest(histoRanges)[1]
    lowerBound = findLowest//10 *10
    upperBound = findHighest//10 *10 + 5
    totalDistance = (upperBound-lowerBound)//5 + 1
    dataListIncrement = totalDistance * [0]
    increment = lowerBound
    for data in range(len(dataListIncrement)):
        dataListIncrement[data] += increment
        increment += 5
        if increment > upperBound:
            break
    #print(f"The scale is: {dataListIncrement}")
    return dataListIncrement

def findLowestHighest(histoRanges):
    findHighest = 0
    for number in histoRanges:
        if number > findHighest:
            findHighest = number

    findLowest = findHighest
    for number in histoRanges:
        if number < findLowest:
            findLowest = number
    #Return value is the highest and lowest values of the list        
    return findHighest, findLowest

def processHistoRangesValues(histoRanges):
    valueList = []
    scale = processHistoRangesScale(histoRanges)
    for index in range(0, len(scale)):
        count = 0
        for data in histoRanges:
            if data >= scale[index] and data < scale[index+1]:
                count += 1
        valueList.append(count)
    #print(f"The values are: {valueList}")
    return valueList
    


def main():
    dataForHistogram = preprocessFile()
    print(f"Scale:  {dataForHistogram[0]}","\n"f"Values: {dataForHistogram[1]}")

##    scaleString = ', '.join([str(data) for data in dataForHistogram[0]])
##    valueString = ', '.join([str(data) for data in dataForHistogram[1]])
##    readyForExcel = f"Scale, {scaleString}"
##    readyForExcel1 = f"Value, {valueString}"
##    print(f"{readyForExcel}",'\n'f"{readyForExcel1}")

main()
