str = "This is a string that contains  and  variables and  more random"
str = int(input("enter a string: "))
num_count = 0
modulus = False
fact = 1
for i in str:
    
    try:
        number = int(i)
        num_count +=1
        print(int(i))
        # check if number is prime
        if number > 1:
            for j in range(2, int(number/2) + 1):
                if (number%j==0):
                    print(f"{number} is not prime")
                    for k in range(number, 1, -1):
                        fact *=int(k)
                        
                    print(f"factorial of {number} is {fact}")
                    fact = 1
                else:
                    print("Number is prime. Performing mod(2)..")
                    if number%2==0:
                        modulus = True
                    else:
                        modulus = False
        
    except ValueError:
        # print('cant parse string to int')
        pass


if(num_count<1):
    print("Could\'t find a number in the string")