from player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == self.name:

            return f"Player {player.name} is already in the guild."

        if player.guild != Player.NO_AFFILIATION:

            return f"Player {player.name} is in another guild."

        self.players.append(player)
        player.guild = self.name

        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player: str) -> str:
        match = next(filter(lambda x: x.name == player, self.players), None)

        if match is None:

            return f"Player {player} is not in the guild."

        self.players.remove(match)
        match.guild = Player.NO_AFFILIATION

        return f"Player {player} has been removed from the guild."

    def guild_info(self) -> str:
        players_info = "\n".join([player.player_info() for player in self.players])

        return f"Guild: {self.name}\n{players_info}"
