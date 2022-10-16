import requests
from bs4 import BeautifulSoup

from base import MidiSong, MidiSongPage, ScrapeFlow

HEADERS = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0",
}


# bitmidi.py
class BitMidi(ScrapeFlow):
    URL = "https://bitmidi.com"

    def front_page(self, url: str) -> list[str]:
        soup = BeautifulSoup(requests.get(url, headers=HEADERS).text, "html.parser")
        return (
            MidiSongPage(a["title"], url + a["href"])
            for a in soup.select_one("div.mv4").find_all("a")
        )

    def song_page(self, song: MidiSongPage) -> MidiSong:
        soup = BeautifulSoup(
            requests.get(song.url, headers=HEADERS).text, "html.parser"
        )

        downloadbtn = soup.select_one(
            "div.fn:nth-child(2) > p:nth-child(2) > a:nth-child(1)"
        )
        return MidiSong(downloadbtn["download"], self.URL + downloadbtn["href"])


if __name__ == "__main__":
    from pprint import pp

    for song in BitMidi():
        pp(song)
