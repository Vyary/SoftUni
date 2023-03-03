from project.album import Album


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album) -> str:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str) -> str:
        try:
            match = next(album for album in self.albums if album.name == album_name)
        except StopIteration:
            return f"Album {album_name} is not found."

        if match.published is True:
            return "Album has been published. It cannot be removed."

        self.albums.remove(match)
        return f"Album {album_name} has been removed."

    def details(self) -> str:
        albums_info = "\n".join([album.details() for album in self.albums])
        return f"Band {self.name}\n{albums_info}"
