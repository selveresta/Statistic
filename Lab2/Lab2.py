import math
import numpy as np
import matplotlib.pyplot as plt


data = []
countData = 0
f = open("result.txt", "w+")


def setData(fileName, data):
    global countData
    file = open(fileName, 'r')
    for line in file:
        data.append(int(line.strip()))

    countData = data.pop(0)


def QPFind(x):
    global data
    sortData = data.copy()
    sortData.sort()

    index = x * (len(sortData) + 1) - 1
    Percentile = sortData[int(index)] + (index % int(index)) * \
        (sortData[int(index) + 1] - sortData[int(index)])
    return Percentile


def StandartDeviation(data):
    sum = 0
    resSum = 0
    for i in data:
        sum += i

    avg = sum / len(data)

    for i in data:
        resSum += (i - avg)**2
    return np.sqrt(resSum/(len(data)-1))


def AverageDeviation(data):
    sum = 0
    totalSum = 0
    for i in data:
        sum += i

    avg = sum / len(data)

    for i in data:
        totalSum += abs(i - avg)

    return totalSum/(len(data))


def boxDiagram(data):
    plt.figure(figsize=(10, 7))
    plt.boxplot(data)
    plt.grid()
    plt.show()


a = (25/129)
b = (10400/129)


def Task2():
    for i in data:
        y = a * i + b
        print(i, y)
        f.write(str(i) + "  " + str(y) + '\n')


setData('./input_10.txt', data)
Q1 = QPFind(1/4)
Q3 = QPFind(3 / 4)
P90 = QPFind(0.9)
print("\n\nQ1 = ", Q1)
f.write("Q1 = " + str(Q1))
print("\nQ3 = ", Q3)
f.write("\nQ3 = " + str(Q3))
print("\nP90 = ", P90)
f.write("\n\nP90e = " + str(P90))


print("\nStandart Deviation = ", StandartDeviation(data))
f.write("\n\nStandart Deviation = " + str(StandartDeviation(data)))
print("Average Deviation = ", AverageDeviation(data))
print("\n")
f.write("\nAverage Deviation = " + str(AverageDeviation(data)) + "\n\n")


Task2()


def StemLeafDiagram():
    global data
    sorted = data.copy()
    sorted.sort()
    stems = []
    print(sorted)
    for i in sorted:
        strI = str(i)[0]
        if (i < 100):
            stems.append(int(strI))

        if i == 100:
            stems.append(10)

    plt.ylabel('Data')

    plt.xlabel('Stems')

    plt.stem(stems, sorted)
    plt.show()


StemLeafDiagram()
boxDiagram(data)
