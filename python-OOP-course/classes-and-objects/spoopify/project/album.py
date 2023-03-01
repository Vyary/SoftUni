from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        self.name = name
        self.songs = [*songs]
        self.published: bool = False

    def add_song(self, song: Song) -> str:
        if self.published is True:

            return "Cannot add songs. Album is published."

        if song in self.songs:

            return "Song is already in the album."

        if song.single is True:

            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str) -> str:
        match = next((x for x in self.songs if x.name == song_name), None)

        if match is None:

            return "Song is not in the album."

        if self.published is True:

            return "Cannot remove songs. Album is published."

        self.songs.remove(match)

        return f"Removed song {song_name} from album {self.name}."

    def publish(self) -> str:
        if self.published is True:

            return f"Album {self.name} is already published."

        self.published = True

        return f"Album {self.name} has been published."

    def details(self):
        songs = "\n".join([f"== {song.get_info()}" for song in self.songs])

        return f"Album {self.name}\n{songs}\n"
