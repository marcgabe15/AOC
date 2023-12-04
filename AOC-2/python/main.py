class Solution:
    def __init__(self):
        self.cubeMap = {
            0: 12, # R
            1: 13, # G
            2: 14  # B
        }
    
    def readFileIntoArray(self):
        file = open("example.txt", "r")
        result = []
        for line in file.readlines():
            result.append(line)
        return result
    
    def getGameNumber(self, s: str):
        return int(s.split(" ")[1])
    
    def getAllValues(self, s: str):
        splitString = s.split(":")
        gameNumber = self.getGameNumber(splitString[0])
        rgbArr = self.getRGBArr(splitString[1])
        return (gameNumber, rgbArr)

    '''
    eg input: 1 red, 10 blue, 5 green
    return (1, 5, 10)
    '''
    def mapRGB(self, rgbString: str):
        splitByComma = rgbString.split(",")
        r = g = b = 0
        for x in splitByComma:
            cleanedValue = x.strip().replace("\n", "")
            if cleanedValue.endswith("red"):
                r += int(cleanedValue.split(" ")[0])
            elif cleanedValue.endswith("green"):
                g += int(cleanedValue.split(" ")[0])
            elif cleanedValue.endswith("blue"):
                b += int(cleanedValue.split(" ")[0])
            else:
                print("what happened {0}".format(cleanedValue))
        return (r,g,b)

    '''
    eg input: 1 red, 10 blue, 5 green;
    return [(1,5,10)]
    '''
    def getRGBArr(self, rgbStr: str):
        rgbStrList = rgbStr.split(';')
        return list(map(self.mapRGB, rgbStrList))
    
    def getAnswer(self,arr):
        result = 0
        for game in arr:
            gameNumber, rgbArr = self.getAllValues(game)
            isPossible = True
            r = g = b = 0
            for cubes in rgbArr:
                r = cubes[0]
                g = cubes[1]
                b = cubes[2]
                if r > 12 or g > 13 or b > 14:
                    isPossible = False
                    break
            result += gameNumber if isPossible else 0
        return result
    
    def getSumOfPowers(self, arr):
        result = 0
        for game in arr:
            gameNumber, rgbArr = self.getAllValues(game)
            r = g = b = 0
            for cubes in rgbArr:
                r = max(r,cubes[0])
                g = max(g, cubes[1])
                b = max(b, cubes[2])
            result += (r*g*b)
        return result
if __name__ == "__main__":
    sol = Solution()
    arr = sol.readFileIntoArray()
    print(sol.getAnswer(arr))
    print(sol.getSumOfPowers(arr))



    

