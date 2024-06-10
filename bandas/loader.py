from .models import Band, Album, Song
import json
from datetime import timedelta

Band.objects.all().delete()
Album.objects.all().delete()
Song.objects.all().delete()


def str_to_timedelta(duration_str):
    parts = duration_str.split(':')
    return timedelta(hours=int(parts[0]), minutes=int(parts[1]), seconds=int(parts[2]))

with open('bandas/json/bandas.json') as f:
    bandas = json.load(f)
    for banda in bandas['bands']:
        Band.objects.create(
            name=banda['name'],
            photo=banda['photo'],
            info=banda['info'],
            yearFormation=banda['yearFormation'],
            genre=banda['genre']
        )

with open('bandas/json/albums.json') as f:
    albums = json.load(f)
    for album_info in albums['albums']:
        banda, _ = Band.objects.get_or_create(name=album_info['band'])
        for album_data in album_info['albums']:
            album, _ = Album.objects.get_or_create(
                title=album_data['title'],
                band=banda,
                cover=album_data['cover'],
                releaseDate=album_data['releaseDate'],
                label=album_data['label'],
            )
            for song_info in album_data['songs']:
                Song.objects.create(
                    album=album,
                    title=song_info['title'],
                    linkSpotify=song_info['linkSpotify'],
                    duration=str_to_timedelta(song_info['duration'])
                )