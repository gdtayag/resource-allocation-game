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
        "goto": _money_NYU},
    {"desc": "Give no money",
        "goto": "results"})

    return text, options

def _money_UMD(caller):
    game = caller.search("game")
    rand = random.randint(2)+1
    if rand == 1:
        text = "UMD's antibody testing is effective towards finding a cure for the virus! You're granted $15,000\n\n"
        caller.db.inventory["Budget"] += 5000
        game.db.stats["Cure Progress"] += random.randint(3)
    if rand == 2:
        text = "UMD's antibody testing was ineffective and people think the results grants them liberty and they infect even more people. You have to spend $5,000 more due to the overwhelming healthcare system\n\n"
        caller.db.inventory["Budget"] -= 15000
        game.db.stats["Number of Sick"] += random.randint(50)

    return "results", {"text": text}

def _money_NYU(caller):
    caller.db.inventory["Budget"] -= 10000
    text = "NYU thanks you for your kind gesture!\n\n"

    return "results", {"text": text}

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

def results(caller, **kwargs):
    game = caller.search("Game")
    players = list(search_tag("pc"))
    if not kwargs:
        string = ""
    else:
        string = kwargs["text"]
    for x in players:
        player = caller.search(x)
        if not player:
            continue
        player.db.inventory["Budget"] += 15000
    stats = game.get_stats()
    for x in stats:
        string += "%s: %s\n" % (x, stats[x])

    return string, None
