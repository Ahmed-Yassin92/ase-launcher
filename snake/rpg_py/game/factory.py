class Factory():
    """Classe qui permet d'importer les personnage"""

    @classmethod
    def get_character(self, class_name):
        """Methode pour retourner chaque personnage"""
        if class_name == "warrior":
            from characters.warrior import Warrior
            return Warrior()
        elif class_name == "archer":
            from characters.archer import Archer
            return Archer()
        elif class_name == "wizzard":
            from characters.wizzard import Wizzard
            return Wizzard()
        elif class_name == "orc":
            from characters.orc import Orc
            return Orc()
        elif class_name == "wolf":
            from characters.wolf import Wolf
            return Wolf()
        elif class_name == "zombie":
            from characters.zombie import Zombie
            return Zombie()