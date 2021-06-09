
import time
import math
import matplotlib.pyplot as plt

myList = list()
hospitalNumbers = 0
studentNumbers = 0
lastIndex = 0
hospitalPref = 0
studentPref = 0
students = list()
rank = 0
space = 0
hospitals = []

def get_file(fileName):
    File = open(fileName, "rt")
    first_line = File.readline().split()
    global hospitalNumbers
    global studentNumbers
    hospitalNumbers = int(first_line[0])
    hospitals.append(hospitalNumbers)
    studentNumbers = int(first_line[1])
    second_line = File.readline().split()
    global space
    space = list(map(lambda x: int(x) , second_line))
    global hospitalPref
    hospitalPref = [[0 for i in range(studentNumbers)] for j in range(hospitalNumbers)]
    for i in range(hospitalNumbers):
        line = File.readline().split()
        for j in range(studentNumbers):
            hospitalPref[i][j] = int(line[j])
    global studentPref
    studentPref = [[0 for i in range(hospitalNumbers)] for j in range(studentNumbers)]
    for i in range(studentNumbers):
        line = File.readline().split()
        for j in range(hospitalNumbers):
            studentPref[i][j] = int(line[j])
    global rank
    rank = [[0 for i in range(hospitalNumbers)] for j in range(studentNumbers)]
    for i in range(studentNumbers):
        for j in range(hospitalNumbers):
            rank[i][studentPref[i][j]] = j
    global students
    students = [-1] * studentNumbers
    global lastIndex
    lastIndex = [0] * hospitalNumbers

    global myList
    for i in range(hospitalNumbers):
        myList.append(i)
    File.close()


def algorithm():

    global myList
    global lastIndex
    global rank
    global studentPref
    global hospitalPref
    global hospitalNumbers
    global studentNumbers
    global space
    global students
    while (len(myList) > 0):
        get = myList.pop(0)
        while(space[get]):
            newPref = hospitalPref[get][lastIndex[get]]
            if (students[newPref] == -1):
                space[get] = space[get] - 1
                students[newPref] = get
            else:
                throne = students[newPref]
                if (rank[newPref][get] < rank[newPref][throne]):
                    myList.append(throne)
                    space[throne] = space[throne] + 1
                    lastIndex[throne] = lastIndex[throne] + 1
                    students[newPref] = get
                    space[get] = space[get] - 1
                else:
                    lastIndex[get] +=1 

    
def give_file (fileName, file_w):
    output = " "
    for s in file_w:
        output+= str(s) + " "
        fileName = fileName.split ('.')[0]+ ".out"
        File = open(fileName, "")
        File.write(output)
        File.close
        print(f" file name: \"{fileName}\"")


def main():
    fileNames = ["input/1-5-5.in", "input/1-10-5.in", "input/3-3-3.in", "input/3-10-3.in", "input/40.in", "input/80.in", "input/160.in", "input/320.in"]
    times = []
    for f in fileNames:
        print(f)
        print('')
        start_time = time.time()
        get_file(f)
        algorithm()
        print(students)
        print('')
        end_time = ((time.time() - start_time) * 1000)
        end_time = round(end_time, 3)
        times.append(end_time)
        print("Time taken in ms: ", end_time)
        print('')
        #give_file(fileName, students)
    plt.plot(hospitals, times)
    plt.ylabel('Time taken in ms')
    plt.xlabel('Number of hospitals')
    plt.show()

main()
