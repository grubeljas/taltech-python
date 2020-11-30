"""Board games."""
from copy import copy


class Statistics:
    """Statistics class."""

    def __init__(self, filename):
        """Statistic constructor."""
        self.file = filename
        self.fullinfo = copy(self.read_file())
        self.info = self.fullinfo[0]
        self.games = self.fullinfo[1]
        self.players = self.fullinfo[3]
        self.number = self.fullinfo[2]

    def read_file(self):
        """Read the file and create player and game objects."""
        matches = []
        games = {}
        game_checker = {}
        players = {}
        i = 0
        with open(self.file, encoding='utf-8') as file:
            lines = file.read().splitlines()
        for line in lines:
            matches.append(line.split(';'))
        for match in matches:
            i += 1
            dict_players = {}
            for player in match[1].split(','):
                if player not in players.keys():
                    players[player] = Player(player)
                players[player].add_game(match[0])
            if match[2] == 'winner':
                dict_players[match[1]] = match[3]
                winner = match[3]
            elif match[2] == 'points':
                dict_players = dict(zip(match[1].split(","), match[3].split(',')))
                winner = max(dict_players, key=lambda x: int(dict_players[x]))
                loser = min(dict_players, key=lambda x: int(dict_players[x]))
            else:
                places = match[3].split(',')
                dict_players = {i + 1: places[i] for i in range(0, len(places))}
                winner = dict_players[1]
                loser = dict_players[len(dict_players)]

            players[winner].winner()
            if match[0] not in game_checker:
                game_checker[match[0]] = Game(match[0], match[2], self)
                games[match[0]] = [match[2], [dict_players]]
            else:
                games[match[0]][1].append(dict_players)
            game_checker[match[0]].add_matches(dict_players)
            game_checker[match[0]].add_winner(winner)
            if match[2] != 'winner':
                game_checker[match[0]].add_loser(loser)
        return [games, game_checker, i, players]

    def get(self, path):
        """Get the right path."""
        paths = path.split('/')[1:]
        if path.startswith('/total'):
            if len(paths) == 1:
                return self.number
            else:
                i = 0
                for game in self.info.values():
                    if paths[1] == game[0]:
                        i += len(game[1])
                return i
        if path.startswith('/player'):
            return self.player(paths)
        if path.startswith('/game'):
            return self.game(paths)

    def player(self, paths):
        """Get player info."""
        if len(paths) == 1:
            return list(self.players.keys())
        elif paths[2] == 'amount':
            return self.players[paths[1]].number
        elif paths[2] == 'favourite':
            return max(self.players[paths[1]].games, key=lambda x: int(self.players[paths[1]].games[x]))
        elif paths[2] == 'won':
            return self.players[paths[1]].won_games

    def game(self, paths):
        """Get game info."""
        if len(paths) == 1:
            return list(self.games.keys())
        elif paths[2] == 'amount':
            return len(self.games[paths[1]].matches)
        elif paths[2] == 'player-amount':
            return self.games[paths[1]].player_amount()
        elif paths[2] == 'most-wins':
            return max(self.games[paths[1]].winners, key=lambda x: self.games[paths[1]].winners[x])
        elif paths[2] == 'most-frequent-winner':
            return max(self.games[paths[1]].rate(), key=lambda x: self.games[paths[1]].rate()[x])
        elif self.games[paths[1]].type != 'winner':
            if paths[2] == 'most-losses':
                return max(self.games[paths[1]].losers, key=lambda x: self.games[paths[1]].losers[x])
            elif paths[2] == 'most-frequent-loser':
                return max(self.games[paths[1]].rate(0), key=lambda x: self.games[paths[1]].rate(0)[x])
            elif paths[2] == 'record-holder' and self.info[paths[1]][0] == 'points':
                return self.games[paths[1]].find_best()


class Player:
    """Player class."""

    def __init__(self, name):
        """Player constructor."""
        self.name = name
        self.games = {}
        self.number = 0
        self.won_games = 0

    def add_game(self, game):
        """Add game and number of matches."""
        if game not in self.games:
            self.games[game] = 1
        else:
            self.games[game] += 1
        self.number += 1

    def winner(self):
        """Add victory."""
        self.won_games += 1


class Game:
    """Game class."""

    def __init__(self, name, type, stat):
        """Game constructor."""
        self.name = name
        self.type = type
        self.winners = {}
        self.losers = {}
        self.stat = stat
        self.matches = []
        self.participants = {}

    def add_matches(self, match):
        """Add match."""
        self.matches.append(match)

    def add_winner(self, person):
        """Add winner."""
        if person not in self.winners:
            self.winners[person] = 1
        else:
            self.winners[person] += 1

    def add_loser(self, person):
        """Add loser."""
        if person not in self.losers:
            self.losers[person] = 1
        else:
            self.losers[person] += 1

    def rate(self, win=1):
        """Show best or worst player."""
        numbers = {}
        if win:
            group = self.winners
        else:
            group = self.losers
        for person in group:
            numbers[person] = group[person] / self.stat.players[person].games[self.name]
        return numbers

    def find_best(self):
        """Show best record."""
        i = 0
        for person in self.winners:
            for match in self.matches:
                if person in match:
                    if int(match[person]) > i:
                        best = person
                        i = int(match[person])
        return best

    def player_amount(self):
        """Count how many people have played in this game."""
        numbers = []
        if self.type != 'winner':
            for group in self.matches:
                numbers.append(len(group))
        else:
            n_of_players = []
            for n in self.matches:
                n_of_players.append(list(n.keys())[0])
            for group in n_of_players:
                numbers.append(len(group.split(',')))
        return max(set(numbers), key=numbers.count)


if __name__ == '__main__':
    st = Statistics('data')
    print(st.info)
    print(st.get('/total/points'))
    print(st.get('/total'))
    print(st.get('/games'))
    print(st.get('/players'))
    print(st.get('/player/kristjan/amount'))
    print(st.get('/player/joosep/favourite'))
    print(st.get('/player/mart/won'))
    print(st.games['terraforming mars'].matches)
    print(st.get('/game/game of thrones/most-wins'))
    print(st.get('/game/game of thrones/most-frequent-winner'))
    print(st.get('/game/terraforming mars/most-frequent-winner'))
    print(st.get('/game/terraforming mars/most-frequent-loser'))
    print(st.get('/game/terraforming mars/record-holder'))
