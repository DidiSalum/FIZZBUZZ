n = 1
print(n)
for i in range(1000):
    n = n + 1
    if n % 3 == 0 and n % 5 != 0:
        print("FIZZ")
    elif n % 5 == 0 and n % 3 != 0:
        print("BUZZ")
    elif n % 5 == 0 and n % 3 == 0:
        print("FIZZBUZZ")
    else:
        print(n)