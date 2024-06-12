def cycle(xs):
    values = list(xs)

    while True:
        for value in values:
            yield value