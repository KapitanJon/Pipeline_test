def funcA():

    a = int(input("Enter the lower limit: "))
    b = int(input("Enter the upper limit: "))
        
    total = 0

    for x in range(a, b+1, 1):
        total = total + x
    print(total)

#funcA()

def funcB():
    f = int(input("Enter a number or 'finish' to stop:"))

    while f:
        print("The square of the entered number is", f**2)
        f = input("Enter a number or 'finish' to stop:")

funcB()
