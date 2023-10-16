from projects_03.players_and_monsters.project import Song
# from projects_02.spoopify.project.song import Song


class Album:
    def __init__(self, name: str, *songs):  # receive one or many songs
        self.name = name
        self.published = False
        self.songs = [x for x in songs]  # handle the args in a list

    def add_song(self, song: Song):
        if self.published:
            return f"Cannot add songs. Album is published."

        if song.single:
            return f"Cannot add {song.name}. It's a single"

        if song in self.songs:
            return "Song is already in the album."

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."

        try:
            current_song = next(filter(lambda s: s.name == song_name, self.songs))
        except StopIteration:
            return "Song is not in the album."

        self.songs.remove(current_song)
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        output = [f"Album {self.name}"]
        [output.append(f"== {s.get_info()}") for s in self.songs]
        return "\n".join(output)
