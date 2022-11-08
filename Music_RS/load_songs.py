import sys, os
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skdsite.settings")

import django
django.setup()

from songreviews.models import Song

def save_song_from_row(song_row):
    song = Song()
    song.id = song_row[0]
    song.title = song_row[1]
    song.save()

if __name__ == "__main__":

    if len(sys.argv) == 2:
        print("Reading from files..", str(sys.argv[1]))
        songsdf = pd.read_csv(sys.argv[1], encoding='latin-1')
        print(songsdf)

        songsdf.apply(
            save_song_from_row,
            axis = 1
        )

        print("There are {} songs".format(Song.objects.count()))

    else:
        print("Please, provide song filepath.")
