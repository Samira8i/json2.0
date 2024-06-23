import json

music = {"zz top": ["strangers", "red"]}


class MusicLibrary:
    def __init__(self, filename):
        self.filename = filename

    def write_data(self, new):
        with open(self.filename, 'w') as f:
            json.dump(new, f)

    def load_data(self):
        with open(self.filename, 'r') as f:
            return json.load(f)

    def add_data(self, group, albums):
        music = self.load_data()
        if music:
            if group in music:
                music[group].extend(albums)
            else:
                music[group] = albums
        else:
            music[group] = albums
        return self.write_data(music)

    def delete_data(self, group):
        music = self.load_data()
        if group in music:
            del music[group]
        return self.write_data(music)

    def search_data_bykey(self, group):
        music = self.load_data()
        if group in music:
            return music[group]
        else:
            return "none"

    def search_data_byvalue(self, album):
        music = self.load_data()
        for key in music:
            if album in music[key]:
                return key
        else:
            return "none"


mymusic = MusicLibrary("mymusic.json")
mymusic.write_data(music)
print(mymusic.load_data())
mymusic.add_data("COOL", ["love", "bestie"])
print(mymusic.load_data())
mymusic.add_data("The Doors", ["lll", "country"])
print(mymusic.load_data())
mymusic.add_data("The Doors", ["cry", "what"])
print(mymusic.load_data())
mymusic.delete_data("zz top")
print(mymusic.load_data())
print(mymusic.search_data_bykey("COOL"))
print(mymusic.search_data_byvalue("cry"))
