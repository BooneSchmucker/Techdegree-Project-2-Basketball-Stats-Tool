import constants
import copy
import sys

players_copy = copy.deepcopy(constants.PLAYERS)
teams_copy = copy.deepcopy(constants.TEAMS)
experienced_players = []
inexperienced_players = []
panthers = []
bandits = []
warriors = []


def clean_data():
    for player in players_copy:
        clean_height = player["height"].split(" ")
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



def display_stats(team):
    total_players = len(team)
    players_names = []
    for name in team:
        players_names.append(name["name"])
    print("-"*26)
    print("\nTotal Players: {}\n".format(total_players))
    print("-"*8, "Players:", "-"*8)
    print(", ".join(players_names))


def console():
    print("Boones Basketball Stats Tool\n")
    print("-"*11, "MENU", "-"*11)
    print("\nChoose your destiny:\n")
    while True:
        try:
            print("1 - Select a team")
            print("2 - Exit the program\n")
            prompt1 = int(input("Enter 1 or 2 > "))
            if prompt1 < 1 or prompt1 > 2:
                print("\nNot a valid selection; Please, enter 1 or 2.\n")
                continue
        except ValueError:
            print("\nNot a valid selection; Please, enter 1 or 2.\n")
        else:
            if prompt1 == 1:
                print("\n")
                print("-"*11, "TEAMS", "-"*11)
                print("\n1 - Panthers")
                print("2 - Bandits")
                print("3 - Warriors\n")
                try:
                    prompt2 = int(input("Select team > "))
                    if prompt2 < 1 or prompt2 > 3:
                        print("\nNot a valid selection; Please, try again\n")
                        continue
                except ValueError:
                    print ("\nNot a valid selection; Please, try again\n")
                else:
                    if prompt2 == 1:
                        print("\nPanthers\n")
                        display_stats(panthers)
                    elif prompt2 == 2:
                        print("\nBandits\n")
                        display_stats(bandits)
                    elif prompt2 == 3:
                        print("\nWarriors\n")
                        display_stats(warriors)
            elif prompt1 == 2:
                break
    sys.exit("\nYou have exited the stats tool. See you next season!\n")

if __name__ == "__main__":
    clean_data()
    balance_teams()
    console()
    display_data()
    