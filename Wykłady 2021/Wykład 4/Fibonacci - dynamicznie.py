from time import perf_counter

#   F1=1
#   F2=1
#   Fn=F(n-1)+F(n-2)


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_dyn(n):
    F=[1]*(n+1)
    for i in range(3,n+1):
        F[i]=F[i-1]+F[i-2]
    return F[n]


n = int(input("Podaj n: "))
if n>35:
    print("To będzie długo trwało, jak jesteś pewien")
    print("to wpisz TAK, jak nie, wpisz NIE, i mniejszą liczbę")
    x=str(input(""))
    if x=="NIE" or x=="nie":
        n = int(input("Podaj ponownie n: "))
    print("Wyniki dla", n)



start=perf_counter()
print(fib(n))
interwal=perf_counter()
print("Zwykłe - %f sec." % (interwal - start))
print(fib_dyn(n))
end=perf_counter()
print("Dynamiczne - %f sec." % (end-interwal))