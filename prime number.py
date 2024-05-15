def prime(num):
    if num >= 1:
        for i in range(2, num):
            if (num % i) ==0:
                print("not a prime number")
                break
            else:
                print("its a prime number")
                break

n = int(input("enter number"))
prime(num=n)