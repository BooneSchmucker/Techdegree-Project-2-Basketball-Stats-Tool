import constants
import copy

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)
experienced_players = []
inexperienced_players = []

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



        
        

if __name__ == "__main__":
    clean_data()