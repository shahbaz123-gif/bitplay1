def setOrNot(number,n):
    mask = 1<<(n-1)

    if number & mask:
        print("SET")
    else:
        print("Not SET")   

number=int(input("Enter No"))
n = int(input("Enter bit position"))
setOrNot(number, n)