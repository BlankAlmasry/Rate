class PlayersContainer:
    def __init__(self):
        self.players = {}

    def add_player(self, name, rating):
        if name in self.players.keys():
            raise ValueError(f"Player {name} already exists")
        self.players[name] = rating

    def get_player(self, name):
        if name not in self.players.keys():
            raise ValueError(f"Player {name} does not exist")
        return self.players[name]

    def update_player(self, key, value):
        if key not in self.players.keys():
            raise ValueError(f"Player {key} does not exist")
        self.players[key] = value

    def __del__(self):
        self.players.clear()
        del self.players
