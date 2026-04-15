def Ofunc(n):
    iteration = 0
    for i in range(0,n):
        for j in range(0,n):
            print("*",end="")
            iteration += 1
        print(" ")
    print(f"n = {n}, Number of iterations = {iteration}")

Ofunc(10)
Ofunc(7)
Ofunc(8)