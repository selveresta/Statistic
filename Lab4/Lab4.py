import numpy as np


def P(b, total):
    return (b / total)


def A(n, m):
    b = (np.math.factorial(n)/np.math.factorial(n - m))
    return b


def fact(n, m):
    b = (np.math.factorial(n) * np.math.factorial(m-3)) / \
        (np.math.factorial(m)*np.math.factorial(n-3))
    return b


def dob_fact(a, p, m, n):
    b = (p / n) * fact(a, m)
    return b


def task1(b, br, r, bl):
    print("Task 1:")
    total = b + br + r + bl
    print("Is Black Box =", (P(b, total)))
    print("Is Brown Box =", (P(br, total)))
    print("Is Red Box =", (P(r, total)))
    print("Is Blue Box =", (P(bl, total)))
    print("Is Blue or Red Box =", (P(bl, total) + P(r, total)))


def task2(n, n1, m):
    print("\nTask 2:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("The probability that at least one will be a consultant=",
          ((A1 - A2) / A1))


def task3(n, n1, m):
    print("\nTask 3:")
    A1 = A(n, m)
    A2 = A(n1, m)
    print("The probability that there will be at least one of the relatives among the selected specialists =",
          ((A1 - A2) / A1))


def task4(p1, p2, p3, p4):
    print("\nTask 4:")
    print("The probability that this item is destined for the fifth department =",
          ((1 - (p1 + p2 + p3 + p4))))


def task5(p1, a1):
    print("\nTask 5:")
    print("The probability of the arrival of two shunting trains on two adjacent tracks =",
          (((p1/a1) * ((p1-1)/(a1-1)))))


def task6(p1, p2):
    print("\nTask 6:")
    print("The probability that the product of the first grade is produced by this machine =",
          ((p1 * p2)))


def task7(p1, p2, p3, p4, a1, a2, a3, a4, m, n):
    print("\nTask 7:")
    b = dob_fact(a1, p1, m, n) + dob_fact(a2, p2, m, n) + \
        dob_fact(a3, p3, m, n) + dob_fact(a4, p4, m, n)
    print("The probability that this student is prepared: \n\t\tа) perfectly = ",
          round((dob_fact(a1, p1, m, n) / b)))
    print("\t\tб) badly = ", round((dob_fact(a4, p4, m, n) / b)))


def task8(p1, p2, p3, a1, a2, a3):
    print("\nTask 8:")
    print("The probability that a piece taken at random is standard =",
          round((((p1*a1) + (p2*a2) + (p3*a3)))))


def task9(p1, p2, p3, a1, a2, a3):
    print("\nTask 9:")  # Формула Байєса
    print("The probability that the patient had peritonitis =",
          round((((p2 * a2)/((p1 * a1) + (p2 * a2) + (p3 * a3))))))


def task10(p1, p2, a1, a2):
    print("\nTask 10:")
    print("The probability that the device is assembled by a highly qualified specialist=",
          round((((p1 * a1) / ((p1 * a1) + (p2 * a2)))), 2))


task1(40, 26, 22, 12)
print("---------------------------------")
task2(10, 2, 2)
print("---------------------------------")

task3(10, 8, 3)
print("---------------------------------")

task4(0.15, 0.25, 0.2, 0.1)
print("---------------------------------")

task5(80, 120)
print("---------------------------------")

task6(0.9, 0.8)
print("---------------------------------")

task7(3, 4, 2, 1, 20, 16, 10, 5, 20, 10)
print("---------------------------------")

task8(0.4, 0.3, 0.3, 0.9, 0.95, 0.95)
print("---------------------------------")

task9(0.4, 0.3, 0.3, 0.8, 0.7, 0.85)
print("---------------------------------")

task10(0.3, 0.7, 0.9, 0.8)
print("---------------------------------")
