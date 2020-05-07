from typeclasses.characters import Character

class NPC(Character):

    def at_object_creation(self):
        stats = {"Number of Dead" : 2000,
        "Number of Sick" : 10000,
        "Discontent" : 500,
        "Cure Progress" : 3,
        "Vaccine Progress" : 5}
        self.db.stats = stats
        self.tags.add("Game")

    def get_stats(self):
        return self.db.stats
