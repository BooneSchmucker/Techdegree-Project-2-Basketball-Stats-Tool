import constants
import copy

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)
experienced_players = []
inexperienced_players = []
panthers = []
bandits = []
warriors = []


def clean_data():
    for player in players_copy:
        clean_height = player["height"].split()
        player["height"] = int(clean_height[0])
        if player["experience"] == "YES":
            player["experience"] = True
            experienced_players.append(player)
        elif player["experience"] == "NO":
            player["experience"] = False
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players


def balance_teams():
    teams = [panthers, bandits, warriors]
    num_teams = len(teams)
    for num in range(len(experienced_players)):
        teams[num % num_teams].append(experienced_players[num])
    for num in range(len(inexperienced_players)):
        teams[num % num_teams].append(inexperienced_players[num])

        
        
    
    
        
        

if __name__ == "__main__":
    clean_data()
    balance_teams()