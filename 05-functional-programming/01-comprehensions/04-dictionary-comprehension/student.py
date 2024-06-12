def title_to_director(movies):
    return {movie.title : movie.director for movie in movies}

def director_to_titles(movies):
    result = {}
    
    for movie in movies:
        if movie.director not in result:
            result[movie.director] = []
        result[movie.director].append(movie.title)
    
    return result
