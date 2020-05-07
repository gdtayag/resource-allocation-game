from evennia.utils import evmenu
from numpy import random

def scenario_1(caller):
    text = "Your people want to go back to work! Should you leave Stay at home orders up or open the country?"
    options = (
    {"desc": "Continue Stay at Home orders",
        "goto": _continue_orders},
    {"desc": "Open the country",
        "goto": _open_country})

    return text, options

def _continue_orders(caller):
    game = caller.search("game")
    game.db.stats["Number of Sick"] -= random.randint(100)
    game.db.stats["Cure Progress"] += random.randint(5)
    game.db.stats["Vaccine Progress"] += random.randint(5)

    return "results"

def _open_country(caller):
    game = caller.search("game")
    game.db.stats["Number of Sick"] += random.randint(500)
    game.db.stats["Cure Progress"] -= random.randint(10)
    game.db.stats["Vaccine Progress"] -= random.randint(10)

    return "results"

def results(caller):
    game = caller.search("Game")

    stats = game.get_stats()
    string = ""
    for x in stats:
        string += "%s: %s\n" % (x, stats[x])

    return string, None
