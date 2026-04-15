def myfunction(n):
    for i in range(0,n+1):
        print("First Loop")
    j=1
    while(j<=n+1):
        print("Second Loop ",j)
        j=j*2
    for i in range(0,100):
        print("Third loop")

def Omyfunction(n):
    iteration = 0
    for i in range(0,n+1):
        iteration +=1
    j=1
    while(j<=n+1):
        iteration +=1
        j=j*2
    for i in range(0,100):
        iteration += 1
    
    print(f"When n is {n}, iterations={iteration}")

Omyfunction(9)
Omyfunction(7)