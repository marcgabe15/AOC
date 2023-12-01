class Solution:
    def __init__(self):
        self.curMap = {
            "one": "1",
            "two": "2",
            "three": "3",
            "four": "4",
            "five": "5",
            "six": "6",
            "seven": "7",
            "eight": "8",
            "nine": "9"
        }
        self.numStr = "one|two|three|four|five|six|seven|eight|nine".split('|')
        print(self.numStr)
        self.starStr = "otfsen"

    def readFileIntoArray(self):
        file = open("example.txt", "r")
        result = []
        for line in file.readlines():
            result.append(line)
        return result

    def findNumbersAndAdd(self, arr):
        currentResult = 0
        for x in arr:
            currentNumber = ""
            for char in x:
                if char in "0123456789":
                    currentNumber += char
            currentResult += int(currentNumber[0] + currentNumber[-1])
        return currentResult

    def findNumbersAndAddTwo(self, arr):
        currentResult = 0
        for x in arr:
            currentNumber = ""
            i = 0
            while i < len(x):
                char = x[i]
                if char in "0123456789":
                    currentNumber += char
                elif char in self.starStr:
                    for y in self.numStr:
                        lenIndex = min(len(arr), i + len(y))
                        if x[i:lenIndex] == y:
                            currentNumber += self.curMap[y]
                i += 1
            currentResult += int(currentNumber[0] + currentNumber[-1])
        return currentResult

if __name__ == "__main__":
    s = Solution()
    arr = s.readFileIntoArray()
    result1 = s.findNumbersAndAdd(arr)
    result2 = s.findNumbersAndAddTwo(arr)
    print(result1)
    print(result2)
    print("The End")