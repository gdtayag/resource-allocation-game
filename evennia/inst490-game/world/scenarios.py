from evennia.utils import evmenu
from numpy import random
from evennia.utils.search import search_tag

def scenario_1(caller):
    text = "Your people want to go back to work! Should you leave Stay at home orders up or open the country?"
    options = (
    {"desc": "Continue Stay at Home orders",
        "goto": _continue_orders},
    {"desc": "Open the country",
        "goto": _open_country})

    return text, options

def scenario_2(caller):
    text = "UMD's Research institution needs $10,000 for antibody testing for Covid 19, but NYU needs $10,000 to help house nurses and doctors"
    options = (
    {"desc": "Give the money to UMD",
        "goto": _money_UMD},
    {"desc": "Give the money to NYU",
        "goto": _money_NYU}
    )

def _money_UMD(caller):
    return "results"

def _money_NYU(caller):
    return "results"

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
    players = list(search_tag("pc"))
    for x in players:
        player = caller.search(x)
        if not player:
            continue
        player.db.inventory["Budget"] += 15000
    stats = game.get_stats()
    string = ""
    for x in stats:
        string += "%s: %s\n" % (x, stats[x])

    return string, None
