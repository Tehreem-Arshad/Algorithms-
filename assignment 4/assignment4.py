def getInput():
    string1 = input("Enter first string: ") # agttgtagct
    string2 = input("Enter second string: ") # agtgctact
    return string1, string2 # agtgtact


class LCS:
    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2
        self.stripSpaces() # stripping white spaces and new lines

        # data for 2d matrix
        self.rows = None
        self.columns = None

        # dynamic array
        self.dynamicHistory = None

        # list containing lcs of two strings
        self.finalAnswer = []

        self.flag = False


    def stripSpaces(self):
        self.string1 = self.string1.strip()
        self.string2 = self.string2.strip()
        self.string1 = self.string1.strip('\n')
        self.string2 = self.string2.strip('\n')

    def initializeData(self):
        self.rows = len(self.string1) + 1
        self.columns = len(self.string2) + 1
        self.dynamicHistory = [[0 for i in range(self.columns)] for j in range(self.rows)]

    def startFinding(self):
        for i in range(1, self.rows):
            for j in range(1, self.columns):
                self.checkMatch(i, j)
                if self.flag == True:
                    self.getMax(i, j)
                    self.flag = False

    def checkMatch(self, arg1, arg2):
        if self.string1[arg1 - 1] == self.string2[arg2 - 1]:
            self.dynamicHistory[arg1][arg2] = self.dynamicHistory[arg1 - 1][arg2 - 1] + 1
        else:
            self.flag = True

    def getMax(self, arg1, arg2):
        self.dynamicHistory[arg1][arg2] = max(self.dynamicHistory[arg1 - 1][arg2], self.dynamicHistory[arg1][arg2 - 1])

    def extractor(self):
        temp1 = self.rows - 1
        temp2 = self.columns - 1
        while temp1 > 0 and temp2 > 0:
            if self.dynamicHistory[temp1][temp2] != self.dynamicHistory[temp1 - 1][temp2]:
                self.finalAnswer.append(self.string1[temp1 - 1])
                temp1 = temp1 - 1
                temp2 = temp2 - 1
            else:
                temp1 = temp1 - 1


def main():
    string1, string2 = getInput()
    longestCommonSubsequence = LCS(string1, string2)
    longestCommonSubsequence.initializeData()
    longestCommonSubsequence.startFinding()
    longestCommonSubsequence.extractor()
    print("LCS of ", string1, " and ", string2, " is: ", ''.join(longestCommonSubsequence.finalAnswer[::-1]))
    
if __name__ == "__main__":
    main()
