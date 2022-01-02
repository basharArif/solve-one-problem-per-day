from math import sqrt

A, B, C = input().split(" ")
A = float(A)
B = float(B)
C = float(C)
value = B * B - 4 * A * C

if A != 0 and value > 0:
    R1 = (-B + sqrt(value)) / (2 * A)
    R2 = (-B - sqrt(value)) / (2 * A)
    print(f'R1 = {R1:.5f}\nR2 = {R2:.5f}')
else:
    print("Impossivel calcular")
