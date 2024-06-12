def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    commons = set()
    for item in xs:
        if(item in ys):
             commons.add(item)

    return commons