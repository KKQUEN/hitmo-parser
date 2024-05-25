import requests
from bs4 import BeautifulSoup


class HitmoParser:
    main_link = r"https://rus.hitmotop.com/"

    def __init__(self):
        self.res_link = self.main_link
        self.track_list = []

    def find_song(self, song_name: str) -> str:
        """
        gets song name
        returns link for find this song
        """
        self.res_link = HitmoParser.main_link + "search?q=" + "+".join(song_name.split())
        return self.res_link

    def get_songs(self, link) -> list:
        """
        gets link on site
        returns songs info (artist, name, duration, download_link)
        """
        self.track_list = []
        r = requests.get(link)
        bs = BeautifulSoup(r.text, features="html.parser")
        tracks = bs.find_all("li", {"class": "tracks__item"})
        for track in tracks:
            track_title = track.find("div", {"class": "track__title"}).text.strip()
            track_artist = track.find("div", {"class": "track__desc"}).text
            track_length = track.find("div", {"class": "track__fulltime"}).text
            track_download_link = track.find("a", {"class": "track__download-btn"})['href']

            track_info = {
                "title": track_title,
                "artist": track_artist,
                "length": track_length,
                "download_link": track_download_link
            }
            self.track_list.append(track_info)
        return self.track_list
