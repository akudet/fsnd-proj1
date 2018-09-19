import media


def favorite_movies():
    """
    :return: a list of my favorite movies
    """

    movies = []

    star_war = media.Movie("Star Wars: The Last Jedi",
                           "https://i.ytimg.com/vi_webp/fgPqJgZepxM/movieposter.webp",
                           "https://www.youtube.com/watch?v=fgPqJgZepxM",
                           )

    the_day_after_tomoorow = media.Movie("The Day After Tomorrow",
                                         "https://i.ytimg.com/vi_webp/K_xwj9bHZm4/movieposter.webp",
                                         "https://www.youtube.com/watch?v=K_xwj9bHZm4",
                                         )

    battleship = media.Movie("Battleship",
                             "https://i.ytimg.com/vi_webp/qcmYSxnYZV4/movieposter.webp",
                             "https://www.youtube.com/watch?v=qcmYSxnYZV4",
                             )

    terminator2 = media.Movie("Terminator 2: Judgment Day",
                              "https://i.ytimg.com/vi_webp/qlqIVb-UxDE/movieposter.webp",
                              "https://www.youtube.com/watch?v=qlqIVb-UxDE",
                              )

    movies.append(star_war)
    movies.append(the_day_after_tomoorow)
    movies.append(battleship)
    movies.append(terminator2)

    return movies
