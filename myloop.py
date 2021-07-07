num = 0
while True:
    num = int(input("enter a number: "))
    if num==12:
        print(f"{num} ... breaking....")
    for i in range(2, int(num/2)):
        if num%i==0:
            print(f"{num} is not prime")
            for j in range(0, num-1):
                if j%2!=0:
                    print(j)
        else:
            print(f"{num} is prime")