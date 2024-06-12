def fizzbuzz():
    current = 1

    while True:
        result = ""
        
        if current % 5 == 0:
            result = "buzz"
        if current % 3 == 0:
            result = "fizz"
        if (current % 3 == 0 and current % 5 == 0):
            result = "fizzbuzz"

        result = result or str(current)

        yield result
        current += 1

ns = fizzbuzz()

print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))
print(next(ns))

