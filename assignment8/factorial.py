def factorial(n):
    if n < 0:
       print("Factorial does not exist for negative numbers")
       return None
    elif n == 0:
       return 1
    else:
       fact=1
    for  i in range(1,n+1):
        fact = fact*i
    print(fact)
factorial(-8)