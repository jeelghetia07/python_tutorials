n = int(input("enter the number : "))
if n > 1 :
    prime = True
    for i in range(2, (n//2)+1):
        if(n % i == 0):
            prime = False
            break
    if prime:
        print("is prime...")
    else:
        print("not prime.")
else:
    print("not prime")

# Output : 
# enter the number : 7
# is prime...

