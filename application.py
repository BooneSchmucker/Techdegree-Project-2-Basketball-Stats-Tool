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
        clean_height = int(player["height"].split(" ")[0])
        clean_guardians = player["guardians"].split(" and ")
        if player["experience"] == "YES":
            player["experience"] = True
            experienced_players.append(player)
        elif player["experience"] == "NO":
            player["experience"] = False
            inexperienced_players.append(player)
    return experienced_players, inexperienced_players, clean_height, clean_guardians


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
    guardians_names = [] #still displying "and" between guardians
    experienced_count = 0
    inexperienced_count = 0
    for name in team:
        players_names.append(name["name"])
    for guardians in team:
        guardians_names.append(guardians["guardians"])
    for player in team:
        if player["experience"] == True:
            experienced_count += 1
        else:
            inexperienced_count += 1
    print("Total Players: {}".format(total_players))
    print("Experienced Players: {}".format(experienced_count))
    print("Rookies: {}".format(inexperienced_count))
    print("\n**Players**")
    print(", ".join(players_names))
    print("\n**Guardians**")
    print(", ".join(guardians_names), "\n")

def console():
    print("Boones Basketball Stats Tool\n")
    print("-"*8, "MENU", "-"*8)
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
                print("-"*8, "TEAMS", "-"*8)
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
                        print("\n**Panthers**")
                        display_stats(panthers)
                    elif prompt2 == 2:
                        print("\n**Bandits**")
                        display_stats(bandits)
                    elif prompt2 == 3:
                        print("\n**Warriors**")
                        display_stats(warriors)
            elif prompt1 == 2:
                break
    sys.exit("\nYou have exited the stats tool. See you next season!\n")

if __name__ == "__main__":
    clean_data()
    balance_teams()
    console()
    display_data()
    