
import datetime
import random
from matplotlib import pyplot as plt

times1 = []
times2 = []

class bruteForce:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.num1Length = None
        self.num2Length = None
        self.output = None
        self.pos1 = None
        self.pos2 = None
        self.finalResult = None
        self.zero = None
        self.zero2 = None
        self.counter = None
        self.transfer = None

    def initializeValues(self):
        self.num1Length = len(self.num1)
        self.num2Length = len(self.num2)
        totalLength = self.num1Length + self.num2Length
        self.output = [0] * (totalLength) 
        self.pos1 = 0
        self.pos2 = 0
        self.finalResult = ""

    def isZero(self):
        if self.num1Length == 0 or self.num2Length == 0:
            self.zero = True
        else:
            self.zero = False
        
    def bruteForceMultiply(self):
        for i in range(self.num1Length - 1, -1, -1):
            self.transfer = 0
            n1 = ord(self.num1[i]) - 48
            self.pos2 = 0
            for j in range(self.num2Length - 1, -1, -1):
                n2 = ord(self.num2[j]) - 48
                summ = n1 * n2 + self.output[self.pos1 + self.pos2] + self.transfer
                self.transfer = summ // 10
                self.output[self.pos1 + self.pos2] = summ % 10
                self.pos2 = self.pos2 + 1
            self.checkState()
            self.pos1 = self.pos1 + 1

    def checkState(self):
        if self.transfer > 0:
            self.output[self.pos1 + self.pos2] = self.output[self.pos1 + self.pos2] + self.transfer


    def rePosition(self):
        self.counter = len(self.output) - 1
        while self.counter >= 0 and self.output[self.counter] == 0: 
            self.counter = self.counter - 1

    def isZero2(self):
        if self.counter == -1: 
            self.zero2 = True
        else:
            self.zero2 = False

    def printer(self):
        while self.counter >= 0: 
            self.finalResult = self.finalResult + chr(self.output[self.counter] + 48) 
            self.counter = self.counter - 1


def testCasesGenerator(digits):
    return random.randint(10 ** (digits - 1), 10 ** digits - 1)  

def bruteHelper(integer_1, integer_2, signal, digits):
    b = bruteForce(integer_1, integer_2)
    b.initializeValues()
    b.isZero()
    if b.zero == True:
        print("Brute force multiplication result: ", "0")
    else:
        b.bruteForceMultiply()
        b.rePosition()
        b.isZero2()
        if b.zero2 == True:
            if signal == True:
                print("Brute force multiplication result: ", "0")
            else:
                print("Brute multiplication of integers with ", digits, " digits completed")
        else:
            b.printer()
            if signal == True:
                print("Brute force multiplication result: ", b.finalResult)
            else:
                print("Brute multiplication of integers with ", digits, " digits completed")

def generateFour(div, signal, t, n1, n2):
    if signal == "//" and t == "first":
        return n1 // (10 ** div)
    elif signal == "%" and t == "first":
        return n1 % (10 ** div)
    elif signal == "//" and t == "second":
        return n2 // (10 ** div)
    elif signal == "%" and t == "second":
        return n2 % (10 ** div)


def daqHelper(integer_1, integer_2):
    integer_1 = int(integer_1)
    integer_2 = int(integer_2)

    if integer_1 < 10 and integer_2 < 10:
        return integer_1 * integer_2

    len1 = len(str(integer_1))
    len2 = len(str(integer_2))

    maximumOfBoth = max(len1, len2)
    div = round(maximumOfBoth / 2)

    temp1 = generateFour(div, "//", "first", integer_1, integer_2)
    temp2 = generateFour(div, "%", "first", integer_1, integer_2)
    temp3 = generateFour(div, "//", "second", integer_1, integer_2)
    temp4 = generateFour(div, "%", "second", integer_1, integer_2)

    temp5 = daqHelper(temp1, temp3)
    temp6 = daqHelper(temp2, temp4)
    finall = daqHelper(temp1 + temp2, temp3 + temp4) - temp5 - temp6

    return (10 ** (2*div))*temp5 + (10 ** div)*finall + temp6


def testAndplot(integer1List, integer2List, samples):
    times1 = []
    times2 = []
    print("Testing for brute force")
    print("")
    for i in range(len(integer1List)):
        start = datetime.datetime.now()
        bruteHelper(str(integer1List[i]), str(integer2List[i]), False, samples[i])
        end = datetime.datetime.now()
        times1.append((end - start).total_seconds() * 1000)

    print("")
    print("Testing for divide and conquer")
    print("")
    for i in range(len(integer1List)):
        start = datetime.datetime.now()
        result = daqHelper(str(integer1List[i]), str(integer2List[i]))
        end = datetime.datetime.now()
        print("Divide and conquer multiplication of integers with ", samples[i], " digits completed")
        times2.append((end - start).total_seconds() * 1000)
    print("")
    
    # Now plotting

    plt.plot(samples, times1, label="Brute force") 
    plt.plot(samples, times2, label="Divide and conquer")
    plt.xlabel('Input size in number of decimal digits') 
    plt.ylabel('Time taken in milliseconds')
    plt.title('Brute force vs Divide and conquer comparison')
    plt.legend()
    plt.savefig('plot.jpeg')


"""
if you input "b" or "B" then first it will take inputs from user and generate results
same approach for divide and conquer algorithm upon inputting "d" or "D"
However, whichever one user selects and runs the program will automatically generate test cases and test
them on both algorithms on its own at the end and generate plots
"""


def main():
    choice = input('Enter B/b for brute force or D/d for divide and conquer: ')
    if choice == 'B' or choice == 'b':
        integer_1 = input("Enter first big integer: ")
        integer_2 = input("Enter second big integer: ") 
        bruteHelper(integer_1, integer_2, True, None)
        print("")
        print("-----------------------------------------------")
        print("")

        # Now generating test cases, executing them, and plotting corresponding graphs

        print("Generating test cases and executing them on both algorithms now")
        print("")

        samples = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        times = []
        integer1List = []
        integer2List = []
        for i in samples:
            integer1List.append(testCasesGenerator(i))
            integer2List.append(testCasesGenerator(i))

        print("Test cases generated! Now executing!")
        print("")
        
        testAndplot(integer1List, integer2List, samples)

        print("Testing completed and graph has been plotted!")

    elif choice == 'D' or choice == 'd':
        integer_1 = input("Enter first big integer: ")
        integer_2 = input("Enter second big integer: ") 
        result = daqHelper(integer_1, integer_2)
        print("Divide and conquer multiplication result: ", result)
        print("")
        print("-----------------------------------------------")
        print("")
        
        # Now generating test cases, executing them, and plotting corresponding graphs

        print("Generating test cases and executing them on both algorithms now")
        print("")

        samples = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]
        times = []
        integer1List = []
        integer2List = []
        for i in samples:
            integer1List.append(testCasesGenerator(i))
            integer2List.append(testCasesGenerator(i))
        
        print("Test cases generated! Now executing!")
        print("")
        
        testAndplot(integer1List, integer2List, samples)

        print("Testing completed and graph has been plotted!")

    else:
        print("Invalid choice!")
        
if __name__ == "__main__":
    main()
