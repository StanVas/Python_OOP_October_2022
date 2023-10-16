from projects_03.players_and_monsters.project import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player in self.players:

            return f"Player {player.name} is already in the guild."

        if player.guild != 'Unaffiliated':

            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str): # basically we can't do it like this we have to use next(filter)
        # if player not in self.players:
        #     return f"Player {player_name.name} is not in the guild."
        # self.players.remove(player_name)
        # player_name.guild = "Unaffiliated"
        # return f"Player {player_name.name} has been removed from the guild."
        try:
            player = next(filter(lambda p: p.name == player_name, self.players))

        except StopIteration:

            return f"Player {player_name} is not in the guild."

        self.players.remove(player)
        player.guild = 'Unaffiliated'

        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = [f"Guild: {self.name}"]
        [result.append(p.player_info()) for p in self.players]

        return "\n".join(result)


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
