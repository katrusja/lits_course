min = int(input("Vvedit nyznju mezhu diapazony "))
max = int(input("Vvedit verhnu mezhu diapazony "))

fib1 = int(0)
fib2 = int(1)

while fib2<max:
    fib = fib1 + fib2
    if fib2 >= min:
        print(fib2)
    fib1 = fib2
    fib2 = fib
