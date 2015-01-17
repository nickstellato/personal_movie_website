import fresh_tomatoes
import media

the_dude = media.Movie("The Big Lebowski",
                       "Someone took the dude's rug",
                       "http://static.tvtropes.org/pmwiki/pub/images/the-big-lebowski.jpg",
                       "https://www.youtube.com/watch?v=cd-go0oBF4Y")

pulp_fiction = media.Movie("Pulp Fiction",
                           "Good luck following these out of order story lines",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/8/82/Pulp_Fiction_cover.jpg/220px-Pulp_Fiction_cover.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

bourne_identity = media.Movie("The Bourne Identity",
                              "CIA agent loses memory and tries to figure it all out again",
                              "http://upload.wikimedia.org/wikipedia/en/thumb/a/ae/BourneIdentityfilm.jpg/220px-BourneIdentityfilm.jpg",
                              "https://www.youtube.com/watch?v=FpKaB5dvQ4g")

thomas_crown = media.Movie("The Thomas Crown Affair",
                           "Art theif?",
                           "http://upload.wikimedia.org/wikipedia/en/thumb/6/66/Thomascrownposter1999.jpg/220px-Thomascrownposter1999.jpg",
                           "https://www.youtube.com/watch?v=B3AlaszZSJU")

oceans_twelve = media.Movie("Oceans 12",
                            "A group of thieves attempt to rob a casino",
                            "http://upload.wikimedia.org/wikipedia/en/thumb/8/83/Ocean%27s12Poster1.gif/220px-Ocean%27s12Poster1.gif",
                            "https://www.youtube.com/watch?v=TSKzL-8RHuw")

social_network = media.Movie("The Social Network",
                             "A young Harvard man creates a new world online",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/7/7a/Social_network_film_poster.jpg/220px-Social_network_film_poster.jpg",
                             "https://www.youtube.com/watch?v=lB95KLmpLR4")

movies = [the_dude, pulp_fiction, bourne_identity, thomas_crown, oceans_twelve, social_network]
fresh_tomatoes.open_movies_page(movies)