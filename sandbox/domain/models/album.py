from typing import Optional


class Album:
    def __init__(self, name: str, artist: str, id: Optional[int] = None):
        self.id = id
        self.name = name
        self.artist = artist
