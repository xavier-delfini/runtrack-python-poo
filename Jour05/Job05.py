def fibonacci(i,b=1,a=0):
    if i>2:
        c=a+b
        a=b
        b=c
        i-=1
        b=fibonacci(i,b,a)

        return b
    else:
        if i==1:
            return a
        else:
            return b
number=int(input("Veuillez entrer le nombre de la suite de Fibonacci souhaité"))
print(fibonacci(number))
