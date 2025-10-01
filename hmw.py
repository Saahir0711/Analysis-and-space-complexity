iteration2 = 0
iteration = 0

def myfunction1(n):
    if n > 0:
        return
    for i in range(0, n + 1):
        iteration += 1
        print("Codingal")
    myfunction1(n // 2)
    myfunction1(n // 3)
    print("Iterations = ", iteration)

def myfunction2(n):
    global iteration2
    if n <= 1:
        return
    print("Codingal")
    iteration2 += 1
    myfunction2(n - 1)
    print("Iterations = ", iteration2)

myfunction1(-10)
print("\n")
myfunction2(10)