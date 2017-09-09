import webbrowser


# This class movie says how to display the movie
class Movie():
    # This init function is the starting function
    def __init__(aravindhan, movie_title, movie_storyline, poster, trailer):
            aravindhan.title = movie_title
            aravindhan.storyline = movie_storyline
            aravindhan.poster_image_url = poster
            aravindhan.trailer_youtube_url = trailer

    # This function opens the movie trailer
    def show_trailer(aravindhan):
            webbrowser.open(aravindhan.trailer_youtube_url)
