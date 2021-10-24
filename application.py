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
        #player["height"].split()
        player["height"] = int(player["height"][0:2])
        player["guardians"] = (", ".join(player["guardians"].split(" and ")))
        if player["experience"] == "YES":
            player["experience"] = True
            experienced_players.append(player)
        elif player["experience"] == "NO":
            player["experience"] = False
            inexperienced_players.append(player)
    return players_copy


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
    guardians_names = []
    experienced_count = 0
    inexperienced_count = 0
    team_height = 0   # not functioning
    for player in team:
        players_names.append(player["name"])
        guardians_names.append(player["guardians"])
        team_height += player["height"]
        if player["experience"] == True:
            experienced_count += 1
        else:
            inexperienced_count += 1
    average_height = round(team_height / len(team))
    print("Total Players: {}".format(total_players))
    print("Experienced Players: {}".format(experienced_count))
    print("Rookies: {}".format(inexperienced_count))
    print("Average Height: {} inches".format(average_height))
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
    