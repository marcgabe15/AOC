def readFileIntoArray():
    file = open("example.txt", "r")
    result = []
    for line in file.readlines():
        result.append(line)
    return result

def findNumbersAndAdd(arr):
    currentResult = 0
    for x in arr:
        currentNumber = ""
        for char in x:
            if char in "0123456789":
                currentNumber += char
        currentResult += int(currentNumber)
    return currentResult

if __name__ == "__main__":
    print("Starting program")
    arr = readFileIntoArray()
    result = findNumbersAndAdd(arr)
    print(result)
    print("The End")