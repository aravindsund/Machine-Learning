import movie
import fresh_tomatoes
# Kabali movie: movie title, storyline, poster image and movie trailer
kabali = movie.Movie("KABALI",
                     "A Kuala Lumpur based don Kabaleeswaran is released "
                     "after spending 25 years in prison on a false charge.",
                     "https://in.bookmyfunction.com/blog/wp-content/uploads/2016/05/Kabali-Movie-Special-Posters-2.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=9mdJV5-eias")
# Meesaya Muruku movie: movie title, storyline, poster image and movie trailer
meesaya_muruku = movie.Movie("MEESAYA MURUKU",
                             "A college student is determined to become a "
                             "successful hip-hop musician.",
                             "http://orig03.deviantart.net/a142/f/2017/005/2/c/meesaya_murukku_by_arumugamkartheeban-daub6qp.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=Ghizg_3uI3E")
# sivaji movie: movie title, storyline, poster image and movie trailer
sivaji = movie.Movie("SIVAJI",
                     "Sivaji returns from the U.S. to invest his money for "
                     "good causes, but seeing his rising popularity, the "
                     "politicians cheat him out of his property. Sivaji "
                     "takes this as a challenge.",
                     "http://moviegalleri.net/wp-content/gallery/sivaji-3d-movie-release-posters/sivaji_3d_movie_release_posters_rajini_shriya_0917616.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=Y7znvurIqRA")
# vikram vedha movie: movie title, storyline, poster image and movie trailer
vikram_vedha = movie.Movie("Vikram Vedha",
                           "The film is a dramatic, action thriller.",
                           "https://upload.wikimedia.org/wikipedia/en/0/03/Vikram_Vedha_poster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=1sVr-uWZPjE")
# baahubali movie: movie title, storyline, poster image and movie trailer
baahubali = movie.Movie("Baahubali: The Beginning",
                        "Baahubali: The Beginning, is an Indian epic "
                        "historical fiction film directed by S.S.Rajamouli.",
                        "https://i.ytimg.com/vi/RIOPLQkRjVk/movieposter.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=CYcKs5fknb8")
# thuppakki movie: movie title, storyline, poster image and movie trailer
thuppakki = movie.Movie("Thuppakki",
                        "In a bomb blast, an army officer apprehends a "
                        "sleeper agent who confesses that more bomb "
                        "attacks are planned around the city. "
                        "The officer impedes the subsequent blasts and "
                        "devices a plan to capture the mastermind behind "
                        "these attacks.",
                        "http://data1.ibtimes.co.in/en/full/321219/quotthuppakkiquot-film-poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=aW_j4pNvG98")
# sultan movie: movie title, storyline, poster image and movie trailer
sultan = movie.Movie("Sultan",
                     "Sultan is a story of Sultan Ali Khan a local "
                     "wrestling champion with the world at his feet as he "
                     "dreams of representing India at the Olympics. "
                     "It's a story of Aarfa a feisty young girl from the "
                     "same small town as Sultan with her own set of dreams.",
                     "https://i.ytimg.com/vi/zjW5Iw4Zy0Y/movieposter.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=wPxqcq6Byq0")
# rab ne bana di movie: movie title, storyline, poster image and movie trailer
rab_ne_bana_di_jodi = movie.Movie("Rab Ne Bana Di Jodi",
                                  "After the wedding ceremony between "
                                  "Surinder Sahni and Taani, Surinder "
                                  "discovers that his new wife cares "
                                  "little for him. When she decides to "
                                  "enter a dance competition, Surinder "
                                  "disguises himself, joins the class and "
                                  "tries to befriend her. Taani soon falls "
                                  "in love with her new dance partner, Raj, "
                                  "unaware that he is in fact her husband.",
                                  "https://upload.wikimedia.org/wikipedia/en/a/ab/Rab_Ne_Bana_Di_Jodi.jpg",  # NOQA
                                  "https://www.youtube.com/watch?v=eBi8syxPd14")  # NOQA
# dangal movie: movie title, storyline, poster image and movie trailer
dangal = movie.Movie("Dangal",
                     "Former wrestler Mahavir Singh Phogat trains young "
                     "daughters Geeta and Babita to follow in his "
                     "footsteps and become world-class grapplers.",
                     "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ4MzQzMzM2Nl5BMl5BanBnXkFtZTgwMTQ1NzU3MDI@._V1_UY1200_CR113,0,630,1200_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")  # NOQA
movies = [kabali, meesaya_muruku, sivaji, vikram_vedha, baahubali,
          thuppakki, sultan, rab_ne_bana_di_jodi, dangal]
fresh_tomatoes.open_movies_page(movies)
