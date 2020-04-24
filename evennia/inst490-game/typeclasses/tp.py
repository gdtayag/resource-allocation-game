from typeclasses.objects import Object

class TP(Object):
    def at_object_creation(self):
        self.db.key = 'Toilet Paper'
        self.db.desc = 'Toilet Paper'
        self.db.gold_value = 5

from evennia import create_object

new_tp = create_object("typeclasses.tp.TP", key="tp")
