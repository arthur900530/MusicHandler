from datetime import datetime

class Music():
    def __init__(self, name, artist, realease_date) -> None:
        self.name = name
        self.artist = artist
        self.release_date = datetime.strptime(realease_date,'%Y-%m-%d')
    
    def print_info(self):
        print(f'Music Info:\nName: {self.name}\nArtist: {self.artist}\nRelease Date: {self.release_date}')
