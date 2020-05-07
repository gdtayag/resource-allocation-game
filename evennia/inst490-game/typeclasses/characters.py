"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""
from evennia import DefaultCharacter
from numpy import random
from evennia.utils import evmenu

class Character(DefaultCharacter):
    """
    The Character defaults to reimplementing some of base Object's hook methods with the
    following functionality:

    at_basetype_setup - always assigns the DefaultCmdSet to this object type
                    (important!)sets locks so character cannot be picked up
                    and its commands only be called by itself, not anyone else.
                    (to change things, use at_object_creation() instead).
    at_after_move(source_location) - Launches the "look" command after every move.
    at_post_unpuppet(account) -  when Account disconnects from the Character, we
                    store the current location in the pre_logout_location Attribute and
                    move it to a None-location so the "unpuppeted" character
                    object does not need to stay on grid. Echoes "Account has disconnected"
                    to the room.
    at_pre_puppet - Just before Account re-connects, retrieves the character's
                    pre_logout_location Attribute and move it back on the grid.
    at_post_puppet - Echoes "AccountName has entered the game" to the room.

    """
    def at_object_creation(self):
        "This is called when object is first created, only."
        inventory = {"Budget":100000,
                     "Toilet Paper":0,
                     "Food":0,
                     "Hand Sanitizer":0,
                     "Cyber Security":0,
                     "Pharmaceuticals":0,
                     "Workforce":0,
                     "Medical Supplies":0}
        self.db.inventory = inventory
        self.tags.add("pc")

    def at_after_move(self, source_location):
        pass

    def get_inventory(self):
        return self.db.inventory

    def end_turn(caller):
        rand = random.randint(2) + 1
        #rand = 1;
        if rand == 1:
            evmenu.EvMenu(caller, "world.scenarios", startnode="scenario_1")
        elif rand == 2:
            evmenu.EvMenu(caller, "world.scenarios", startnode="scenario_2")
