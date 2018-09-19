import media


def favorite_movies():
    """
    :return: a list of my favorite movies
    """

    movies = []

    star_war = media.Movie("Star Wars: The Last Jedi",
                           "https://i.ytimg.com/vi_webp/fgPqJgZepxM/movieposter.webp",  # NOQA
                           "https://www.youtube.com/watch?v=fgPqJgZepxM",  # NOQA
                           )

    the_day_after_tomoorow = media.Movie("The Day After Tomorrow",
                                         "https://i.ytimg.com/vi_webp/K_xwj9bHZm4/movieposter.webp",  # NOQA
                                         "https://www.youtube.com/watch?v=K_xwj9bHZm4",  # NOQA
                                         )

    battleship = media.Movie("Battleship",
                             "https://i.ytimg.com/vi_webp/qcmYSxnYZV4/movieposter.webp",  # NOQA
                             "https://www.youtube.com/watch?v=qcmYSxnYZV4",  # NOQA
                             )

    terminator2 = media.Movie("Terminator 2: Judgment Day",
                              "https://i.ytimg.com/vi_webp/qlqIVb-UxDE/movieposter.webp",  # NOQA
                              "https://www.youtube.com/watch?v=qlqIVb-UxDE",  # NOQA
                              )

    movies.append(star_war)
    movies.append(the_day_after_tomoorow)
    movies.append(battleship)
    movies.append(terminator2)

    return movies
