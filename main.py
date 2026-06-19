import random

player_team = [
    {"name": "🐹Pikachu", "hp": 100, "moves": {"Thunderbolt": 30, "Quick Attack": 18, "Iron Tail": 25}},
    {"name": "🐲Charizard", "hp": 120, "moves": {"Flamethrower": 32, "Slash": 20, "Dragon Claw": 28}},
    {"name": "🐸Froakie", "hp": 90, "moves": {"Water Pulse": 26, "Quick Attack": 18, "Bubble": 20}},
    {"name": "🦆Golduck", "hp": 110, "moves": {"Aqua Tail": 30, "Confusion": 24, "Water Gun": 22}},
    {"name": "🦧Infernape", "hp": 115, "moves": {"Flame Wheel": 30, "Mach Punch": 24, "Close Combat": 35}},
    {"name": "🦄Bayleef", "hp": 105, "moves": {"Razor Leaf": 28, "Vine Whip": 22, "Body Slam": 26}},
    {"name": "🦕Ivysaur", "hp": 105, "moves": {"Vine Whip": 24, "Razor Leaf": 28, "Tackle": 18}},
    {"name": "🗿Golem", "hp": 130, "moves": {"Rock Throw": 28, "Earthquake": 35, "Tackle": 18}},
    {"name": "🦖Tyranitar", "hp": 140, "moves": {"Bite": 26, "Rock Slide": 32, "Crunch": 30}},
    {"name": "🦅Hawlucha", "hp": 100, "moves": {"Karate Chop": 26, "Flying Press": 32, "Quick Attack": 18}}
]

gyms = {
    "east": {
        "name": "Rock Gym",
        "badge": "Rock Badge",
        "pokemon": [
            {"name": "🐍Onix", "hp": 95, "moves": {"Rock Throw": 22, "Bind": 16, "Stone Edge": 30}},
            {"name": "🦏Rhyhorn", "hp": 100, "moves": {"Horn Attack": 20, "Rock Blast": 24, "Stomp": 18}},
            {"name": "🪾Sudowoodo", "hp": 90, "moves": {"Rock Tomb": 23, "Low Kick": 21, "Mimic Smash": 26}}
        ]
    },
    "west": {
        "name": "Grass Gym",
        "badge": "Grass Badge",
        "pokemon": [
            {"name": "🦙Chikorita", "hp": 85, "moves": {"Razor Leaf": 22, "Vine Whip": 18, "Tackle": 15}},
            {"name": "🍝Tangela", "hp": 95, "moves": {"Mega Drain": 24, "Vine Lash": 21, "Grass Knot": 27}},
            {"name": "🦊Leafeon", "hp": 100, "moves": {"Leaf Blade": 30, "Quick Attack": 18, "Magical Leaf": 25}}
        ]
    },
    "north": {
        "name": "Water Gym",
        "badge": "Water Badge",
        "pokemon": [
            {"name": "🐢Squirtle", "hp": 85, "moves": {"Water Gun": 20, "Tackle": 15, "Aqua Jet": 23}},
            {"name": "🌟Starmie", "hp": 100, "moves": {"Water Pulse": 25, "Swift": 20, "Bubble Beam": 28}},
            {"name": "🦭Lapras", "hp": 115, "moves": {"Aqua Tail": 30, "Ice Shard": 24, "Water Blast": 32}}
        ]
    },
    "south": {
        "name": "Fire Gym",
        "badge": "Fire Badge",
        "pokemon": [
            {"name": "🐶Growlithe", "hp": 90, "moves": {"Ember": 20, "Bite": 18, "Flame Wheel": 25}},
            {"name": "🦆Magmar", "hp": 105, "moves": {"Fire Punch": 28, "Smog": 20, "Flamethrower": 32}},
            {"name": "🦊Flareon", "hp": 100, "moves": {"Fire Fang": 26, "Quick Attack": 18, "Lava Burst": 30}}
        ]
    }
}

garry_team = [
    {"name": "🐢Blastoise", "hp": 125, "moves": {"Hydro Pump": 35, "Aqua Tail": 30, "Bite": 22}},
    {"name": "🌑Umbreon", "hp": 120, "moves": {"Dark Pulse": 30, "Quick Attack": 18, "Shadow Bite": 27}},
    {"name": "⚡Electivire", "hp": 125, "moves": {"Thunder Punch": 32, "Shock Wave": 28, "Low Kick": 24}},
    {"name": "🔥Arcanine", "hp": 130, "moves": {"Flamethrower": 34, "Fire Fang": 28, "Extreme Speed": 30}}
]

badges = []


def choose_team(team, count):

    selected_team = []
    selected_indexes = []

    print("\nChoose your 3 Pokémon")
    print("You cannot choose the same Pokémon twice.\n")

    for i, pokemon in enumerate(team):
        print(f"{i+1}. {pokemon['name']} (HP {pokemon['hp']})")

    while len(selected_team) < count:

        try:
            choice = int(
                input(
                    f"\nChoose Pokémon {len(selected_team)+1}: "
                )
            ) - 1

            if choice < 0 or choice >= len(team):
                print("Invalid selection.")
                continue

            if choice in selected_indexes:
                print("❌ This Pokémon was already selected.")
                print("Choose another Pokémon.")
                continue

            selected_indexes.append(choice)

            pokemon = team[choice].copy()

            pokemon["moves"] = team[choice]["moves"]

            pokemon["current_hp"] = pokemon["hp"]

            pokemon["move_history"] = []

            selected_team.append(pokemon)

            print(f"✅ {pokemon['name']} added!")

        except ValueError:
            print("Enter numbers only.")

    print("\nYour Team:")

    for pokemon in selected_team:
        print(f"• {pokemon['name']}")

    return selected_team


def choose_alive_pokemon(team):
    alive_pokemon = [p for p in team if p["current_hp"] > 0]

    if not alive_pokemon:
        return None

    print("\nChoose your next Pokémon:")

    for i, pokemon in enumerate(alive_pokemon):
        print(f"{i + 1}. {pokemon['name']} - HP: {pokemon['current_hp']}")

    try:
        choice = int(input("Enter Pokémon number: ")) - 1

        if 0 <= choice < len(alive_pokemon):
            return alive_pokemon[choice]
        else:
            print("Invalid choice. First available Pokémon selected.")
            return alive_pokemon[0]

    except ValueError:
        print("Invalid input. First available Pokémon selected.")
        return alive_pokemon[0]


def can_use_move(pokemon, move_name):
    history = pokemon["move_history"]

    if move_name not in history:
        return True

    last_used_index = len(history) - 1 - history[::-1].index(move_name)
    moves_after = len(history) - last_used_index - 1

    if moves_after >= 2:
        return True
    else:
        return False


def choose_enemy_move(enemy_pokemon):
    moves = list(enemy_pokemon["moves"].items())
    available_moves = []

    for move_name, damage in moves:
        if can_use_move(enemy_pokemon, move_name):
            available_moves.append((move_name, damage))

    if available_moves:
        return random.choice(available_moves)
    else:
        return random.choice(moves)


def prepare_enemy_team(team):
    prepared_team = []

    for pokemon in team:
        copy_pokemon = pokemon.copy()
        copy_pokemon["current_hp"] = copy_pokemon["hp"]
        copy_pokemon["move_history"] = []
        prepared_team.append(copy_pokemon)

    return prepared_team


def battle(player_battle_team, enemy_team):
    player_pokemon = choose_alive_pokemon(player_battle_team)
    enemy_index = 0
    enemy_pokemon = enemy_team[enemy_index]

    print(f"\nBattle Started: {player_pokemon['name']} vs {enemy_pokemon['name']}")

    while True:
        if player_pokemon is None:
            print("\nAll your Pokémon fainted!")
            return False

        if enemy_index >= len(enemy_team):
            print("\nYou defeated all enemy Pokémon!")
            return True

        print(f"\nYour Pokémon: {player_pokemon['name']} HP: {player_pokemon['current_hp']}")
        print(f"Enemy Pokémon: {enemy_pokemon['name']} HP: {enemy_pokemon['current_hp']}")

        print("\nChoose a move:")
        moves = list(player_pokemon["moves"].items())

        for i, move in enumerate(moves):
            move_name = move[0]
            damage = move[1]

            if can_use_move(player_pokemon, move_name):
                print(f"{i + 1}. {move_name} - Damage: {damage}")
            else:
                print(f"{i + 1}. {move_name} - COOLING DOWN")

        try:
            move_choice = int(input("Enter move number: ")) - 1

            if 0 <= move_choice < len(moves):
                move_name = moves[move_choice][0]
                damage = moves[move_choice][1]

                if can_use_move(player_pokemon, move_name):
                    enemy_pokemon["current_hp"] -= damage
                    player_pokemon["move_history"].append(move_name)
                    print(f"{player_pokemon['name']} used {move_name}! Damage: {damage}")
                else:
                    print(f"{move_name} is cooling down! You missed your turn.")
            else:
                print("Invalid move! You missed your turn.")

        except ValueError:
            print("Invalid input! You missed your turn.")

        if enemy_pokemon["current_hp"] <= 0:
            print(f"\n{enemy_pokemon['name']} fainted!")

            enemy_index += 1

            if enemy_index >= len(enemy_team):
                print("\nYou won the battle!")
                return True

            enemy_pokemon = enemy_team[enemy_index]
            print(f"\nEnemy trainer sends out {enemy_pokemon['name']}!")
            continue

        enemy_move_name, enemy_damage = choose_enemy_move(enemy_pokemon)
        player_pokemon["current_hp"] -= enemy_damage
        enemy_pokemon["move_history"].append(enemy_move_name)

        print(f"{enemy_pokemon['name']} used {enemy_move_name}! Damage: {enemy_damage}")

        if player_pokemon["current_hp"] <= 0:
            print(f"\n{player_pokemon['name']} fainted!")
            player_pokemon = choose_alive_pokemon(player_battle_team)

            if player_pokemon is not None:
                print(f"\nYou sent out {player_pokemon['name']}!")


def gym_battle(direction):
    gym = gyms[direction]

    if gym["badge"] in badges:
        print(f"\nYou already won the {gym['badge']}.")
        return

    print(f"\nWelcome to the {gym['name']}!")
    print("Both trainers will use 3 Pokémon.")

    player_battle_team = choose_team(player_team, 3)
    gym_pokemon = prepare_enemy_team(gym["pokemon"])

    win = battle(player_battle_team, gym_pokemon)

    if win:
        badges.append(gym["badge"])
        print(f"\nCongratulations! You earned the {gym['badge']}!")
    else:
        print("\nYou lost the gym battle. Try again!")


def johto_league():
    global badges

    if len(badges) < 4:
        print("\nYou cannot enter Johto League.")
        print("Collect all 4 badges first.")
        return False

    print("\nJOHTO LEAGUE FINAL")
    print("You vs Garry")
    print("League Battle: 3 Pokémon vs 3 Pokémon")

    player_battle_team = choose_team(player_team, 3)

    selected_garry_team = random.sample(garry_team, 3)
    garry_battle_team = prepare_enemy_team(selected_garry_team)

    print("\nGarry selected his 3 Pokémon randomly.")

    win = battle(player_battle_team, garry_battle_team)

    if win:
        print("\nGarry lost lol!🔥")
        print("You are the Johto League Champion!🏆")
        print("You are now a Pokémon Master!🧢")
        print("\nGAME OVER - YOU WON!")
        return True

    else:
        print("\nGarry defeated you!🤣")
        print("You lost all your badges.😭")
        print("Start again from the first gym.")

        badges.clear()
        return False
print("======================================")
print("       POKÉMON MASTER ASHES")
print("======================================")
print("You are in Johto City.")
print("Move around and collect all 4 badges.")
print("East  = Rock Gym")
print("West  = Grass Gym")
print("North = Water Gym")
print("South = Fire Gym")
print("League = Register for Johto League")
print("Exit = Quit game")

while True:

    print("\nYou are standing in Johto City.")
    print("Badges collected:", badges)

    direction = input("\nWhere do you want to go? ").lower()

    if direction == "east":
        gym_battle("east")

    elif direction == "west":
        gym_battle("west")

    elif direction == "north":
        gym_battle("north")

    elif direction == "south":
        gym_battle("south")

    elif direction == "league":

        game_finished = johto_league()

        if game_finished:
            break

    elif direction == "exit":
        print("\nThanks for playing Pokémon Johto League Simulator!")
        break

    else:
        print("Invalid direction.")