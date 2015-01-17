import fresh_tomatoes
import media

the_dude = media.Movie("The Big Lebowski",
                       "Someone took the dude's rug",
                       "http://static.tvtropes.org/pmwiki/pub/images/the-big-lebowski.jpg",
                       "https://www.youtube.com/watch?v=cd-go0oBF4Y")

movies = [the_dude]
fresh_tomatoes.open_movies_page(movies)

