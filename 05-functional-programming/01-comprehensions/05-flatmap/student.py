from util import Card

def genres(movies):
    return {genre for movie in movies for genre in movie.genres}

# def actors(movies):
#     return {actor for movie in movies for actor in movie.actors}

def actors(movies):
    actors = set()

    for movie in movies:
        for actor in movie.actors:
            actors.add(actor)

    return actors

# def repeat_consecutive(xs, k):
#     return [x for x in xs for _ in range(k)]

def repeat_consecutive(xs, n):
    result = []

    for x in xs:
        for _ in range(n):
            result.append(x)

    return result

# def repeat_alternating(xs, k):
#     return [x for _ in range(k) for x in xs]

def repeat_alternating(xs, n):
    result = []

    for _ in range(n):
        for x in xs:
            result.append(x)

    return result

def cards(values, suits):
    result = set()

    for value in values:
        for suit in suits:
            result.add(Card(value, suit))

    return result

def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}
