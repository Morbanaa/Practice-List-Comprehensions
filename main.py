# Practicing List Comprehensions

# Challenge One
scores = [12, 45, 67, 23, 89, 34, 90, 56, 11, 78]
new_scores = [score for score in scores if score >= 50]
print(f"Scores >= 50: {new_scores}")

# Challenge Two
prices = [10, 25, 50, 75, 100]
new_prices = [price + price * .2 for price in prices]
print(f"Prices + 20%: {new_prices}")

# Challenge Three
levels = [1, 5, 12, 8, 20, 3, 15, 7, 25]
new_levels = [level * 2 for level in levels if level > 10]
print(f"New Levels: {new_levels}")

# Challenge Four
inventory = [
    {"name": "Iron Sword", "quantity": 1, "value": 80},
    {"name": "Health Potion", "quantity": 4, "value": 15},
    {"name": "Diamond", "quantity": 12, "value": 50},
    {"name": "Wooden Shield", "quantity": 1, "value": 25},
    {"name": "Gold Coin", "quantity": 100, "value": 1},
    {"name": "Magic Staff", "quantity": 1, "value": 150}
]
new_inventory = [
    row["name"]
    for row in inventory
    if row["quantity"] * row["value"] >= 100
    ]
print(f"New Inventory Value > 100: {new_inventory}")

# Challenge Five
players = [
    {"name": "Sora", "kills": 15, "deaths": 3},
    {"name": "Fenrir", "kills": 8, "deaths": 6},
    {"name": "Silvara", "kills": 22, "deaths": 4},
    {"name": "Tarhun", "kills": 5, "deaths": 10},
    {"name": "Jotunn", "kills": 18, "deaths": 2}
]
new_players_list = [
    f"{row["name"]} {str((row["kills"] / row["deaths"]))}"
    for row in players
    if row["deaths"] > 0 and (row["kills"] / row["deaths"]) > 3
]
print(f"Kill ratio over 3: {new_players_list}")

# Challenge Six
dungeon = [
    ["#", "#", "#", "#", "#"],
    ["#", " ", " ", "G", "#"],
    ["#", "T", " ", " ", "#"],
    ["#", " ", "G", "T", "#"],
    ["#", "#", "#", "#", "#"]
]
goblin_list = [
    (iy,ix)
    for iy, y in enumerate(dungeon)
    for ix, x in enumerate(y)
    if x == "G"
]
print(f"Goblins Cords: {goblin_list}")

# Challenge Seven
players = [
    {"name": "Sora", "inventory": ["Sword", "Potion", "Bow"]},
    {"name": "Fenrir", "inventory": ["Staff", "Potion"]},
    {"name": "Silvara", "inventory": ["Axe", "Shield", "Potion"]},
    {"name": "Tarhun", "inventory": ["Sword", "Shield"]}
]
every_item = [
    item
    for row in players
    for item in row["inventory"]
]
print(f"Every Item: {every_item}")

# Challenge Eight
players = [
    {
        "name": "Sora",
        "level": 15,
        "inventory": [
            {"name": "Sword", "value": 100},
            {"name": "Potion", "value": 15},
            {"name": "Diamond", "value": 200}
        ]
    },
    {
        "name": "Fenrir",
        "level": 8,
        "inventory": [
            {"name": "Staff", "value": 150},
            {"name": "Potion", "value": 15}
        ]
    },
    {
        "name": "Silvara",
        "level": 20,
        "inventory": [
            {"name": "Axe", "value": 120},
            {"name": "Shield", "value": 80},
            {"name": "Gem", "value": 300}
        ]
    }
]
items = [
    data["name"]
    for player in players
    for data in player["inventory"]
    if player["level"] > 10 and data["value"] > 100
]
print(f"Items over 100 from level > 10: {items}")

# Challange Nine
temperatures = [12, 25, 31, 8, 19, 35, 4, 28]
temp_list = [
    "Hot" if temp > 25
    else "Cold" if temp < 10
    else "Normal"
    for temp in temperatures
]
print(f"Temp as string: {temp_list}")

# Challange Ten
names = ["Sora", "Fenrir", "Silvara", "Tarhun"]
levels = [15, 8, 20, 25]
data = zip(names,levels)
name_level = [
    f"{name}: Level: {level}"
    for name,level in data
]
print(f"Name and Level: {name_level}")

# Challange Eleven
items = [
    "Sword", "Potion", "Sword", "Shield",
    "Potion", "Bow", "Axe", "Bow"
]
unique_items = [
    item
    for index, item in enumerate(items)
    if item not in items[:index]
]
print(f"Unique Items: {unique_items}")

# Challenge 12
dungeon = [
    ["#", " ", "G", " "],
    ["T", " ", "#", "G"],
    [" ", "G", " ", " "],
    ["#", " ", "T", " "]
]
cords = [
    (iy,ix)
    for iy, y in enumerate(dungeon)
    for ix, x in enumerate(y)
    if x == "G" or x == "T"
]
print(f"Goblin/Treasure Cords: {cords}")

# Challange 13
players = [
    {
        "name": "Sora",
        "stats": {"strength": 80, "speed": 95}
    },
    {
        "name": "Fenrir",
        "stats": {"strength": 95, "speed": 60}
    },
    {
        "name": "Silvara",
        "stats": {"strength": 75, "speed": 90}
    },
    {
        "name": "Tarhun",
        "stats": {"strength": 90, "speed": 85}
    }
]
player_list = [
    player["name"]
    for player in players
    if (player["stats"]["strength"] + player["stats"]["speed"]) >= 170
]
print(f"Players over 170: {player_list}")

# Challange 14
inventory = [
    {"name": "Iron Sword", "value": 80},
    {"name": "Diamond", "value": 500},
    {"name": "Potion", "value": 15},
    {"name": "Magic Staff", "value": 250},
    {"name": "Shield", "value": 100}
]
sorted_list = [
    item["name"]
    for item in sorted(
        inventory,
        key=lambda item: item["value"],
        reverse=True
    )
]
print(f"High to low: {sorted_list}")
