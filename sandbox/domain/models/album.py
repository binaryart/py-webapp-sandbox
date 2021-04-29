from typing import Optional


class Album:
    def __init__(self, name: str, artist: str, guid: Optional[int] = None):
        self.guid = guid
        self.name = name
        self.artist = artist
