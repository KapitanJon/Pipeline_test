"""Outputs the sum of two ranges"""
def func_A():
"""Asks for range input"""
    a = int(input("Enter the lower limit: "))
    b = int(input("Enter the upper limit: "))        
    total = 0
    for x in range(a, b+1, 1):
        total = total + x
    print(total)
func_A()
def func_B():
    """Asks for exit"""
    f = int(input("Enter a number or 'finish' to stop:"))
    while f:
        print("The square of the entered number is", f**2)
        f = input("Enter a number or 'finish' to stop:")
funcB()
