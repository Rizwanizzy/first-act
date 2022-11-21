from omdbapi.movie_search import GetMovie

movie = GetMovie(api_key="cce66885")
name = input("enter movie title:")
details = movie.get_movie(title=name)
data = movie.get_data('title', 'runtime', 'genre', 'actors', 'imdbrating', 'boxoffice')
for i, j in data.items():
    print(i, j)
