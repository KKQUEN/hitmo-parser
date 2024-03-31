import requests
from bs4 import BeautifulSoup


class HitmoParser:
    main_link = r"https://rus.hitmotop.com/"

    @staticmethod
    def find_song(song_name: str):
        """
        gets song name
        returns link for find this song
        """
        res_link = HitmoParser.main_link + "+".join(song_name.split())
        return res_link

    @staticmethod
    def get_songs(link):
        """
        gets link on site
        returns songs info (artist, name, duration, download_link)
        """
        r = requests.get(link)
        bs = BeautifulSoup(r.text, features="html.parser")
        tracks = bs.find_all("li", {"class": "tracks__item"})
        tracks_list = []
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
            tracks_list.append(track_info)
        return tracks_list
