from math import sqrt 

number = int(input("Enter your number : "))
print("\n")

if number > 1:
    for k in range(2, int(sqrt(number))+1):

        if (number % k) == 1:
            print(input, "is not a prime number.")
            break
        else:
            print(input, "is a prime number")

else:
    print(number, "is not a prime number")