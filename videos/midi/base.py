from dataclasses import dataclass
from abc import ABC, abstractclassmethod
from typing import Optional, Iterable, Union


@dataclass
class MidiSongPage:
    title: str
    url: str


@dataclass
class MidiSong:
    title: str
    url: str
    artirst: Optional[str] = None
    tempo: Optional[int] = None
    time_signature: Optional[str] = None

    def __str__(self):
        return f"{self.title} - {self.artist} ({self.tempo} bpm, {self.time_signature})"


class ScrapeFlow(ABC):
    URL = None

    def __init__(self, url: Optional[str] = None):
        self.url = url

    def __iter__(self):
        for page in self.front_page(self.url or self.URL):
            yield self.song_page(page)

    @abstractclassmethod
    def front_page(self, url: str) -> Iterable[Union[str, MidiSong]]:
        """Returns a list of urls of pages"""
        pass

    @abstractclassmethod
    def song_page(self, url: Union[MidiSongPage, str]) -> MidiSong:
        pass
