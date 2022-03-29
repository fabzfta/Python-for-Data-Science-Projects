#What are the genres of the most popular movies?

#A database containing a hige list of movies
#A database with movies by genres
#A database with a lot o popular movies

import pandas as pd
import matplotlib.pyplot as plt

# Use right join to merge the movie_to_genres and pop_movies tables
genres_movies = movie_to_genres.merge(pop_movies, how='right',
                                     left_on="movie_id",
                                      right_on="id")

# Count the number of genres
genre_count = genres_movies.groupby('genre').agg({'id':'count'})

# Plot a bar chart of the genre_count
genre_count.plot(kind='bar')
plt.show()

#The plot says that the most popular genre is Adventure.