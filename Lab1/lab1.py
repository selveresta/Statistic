import math
import numpy
import matplotlib.pyplot as plt


def setData(fileName, data):
    file = open(fileName, 'r')
    for line in file:
        data.append(int(line.strip()))


def getN(data):
    N = 0
    for i in data:
        N += i
    return N


def printTable(data):
    print("Xi\t fi\t Rf\t\t Fi\t")
    count = 1
    N = getN(data)
    Cum = 0
    for i in data:
        Cum += i
        print(count, "\t", i, "\t", round(i/N, 3), "\t\t", Cum)
        count += 1
    print("Total\t", N, "\t", " ", "\t", " ")


data = []

setData('input_100.txt', data)

# Firts Exersice
printTable(data)
print("MAX - ", max(data))

print("\n\n")
# Second Exercise
print("Moda - ", max(set(data), key=data.count))


sortData = data.copy()
sortData.sort()
print("Mediana - ", sortData[int(len(sortData)/2)] if len(sortData) % 2 !=
      0 else (sortData[int(len(sortData)/2) - 1] + sortData[int(len(sortData)/2)]))


# third exercise
rangeD = max(data) - min(data)
upper = 0
for i in data:
    upper += (i - numpy.average(data)) ** 2

dispersion = (upper / (len(data) - 1))

print("MDA = ", dispersion)

sqlrDisper = math.sqrt(dispersion)
print("Середнє квадратичне відхилення розподілу: ", sqlrDisper)


plt.bar(range(len(data)), data)

plt.xlabel("Film")
plt.ylabel("Частота")
plt.show()
