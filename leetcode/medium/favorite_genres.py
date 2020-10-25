def solve(user_songs, genre_to_songs):
    output = {}
    song_to_genre = {}

    if len(user_songs) == 0 or len(genre_to_songs) == 0:
        return output

    for genre in genre_to_songs:
        for song in genre_to_songs[genre]:
            song_to_genre[song] = genre

    for user in user_songs:
        user_genres = {}
        genre_max = 0
        for song in user_songs[user]:
            if user_genres.get(song_to_genre[song]) is None:
                user_genres[song_to_genre[song]] = 1
            else:
                user_genres[song_to_genre[song]] += 1

            if genre_max < user_genres[song_to_genre[song]]:
                genre_max = user_genres[song_to_genre[song]]

        output[user] = [g for g in user_genres.keys() if user_genres[g] == genre_max]

    return output


if __name__ == '__main__':
    print('Favorite genres')

    userSongs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"]
    }
    songGenres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }

    # userSongs = {
    #                 "David": ["song1", "song2"],
    #                 "Emma": ["song3", "song4"]
    #             },
    # songGenres = {}

    print(solve(userSongs, songGenres))
