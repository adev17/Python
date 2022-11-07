#Patterns in a4_output file: The file starts with a large number 10,000 which
#is subtracted by a variable number (100), from there, the variable continuously decreases by 1 until it
#(variables value) reaches 10 and then resets back to 100. The loop ends when the large starting number
#(10,000) reaches 0.

D = 100
C = 10000
while C >= 0:
    print(C)
    C = C - D
    if (D == 10): D = 100
    else: D = D - 1





