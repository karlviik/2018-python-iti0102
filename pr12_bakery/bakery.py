"""Do bake."""


class Baker:
    """Baker class for bakers."""

    def __init__(self, name: str, experience_level: int, money: int):
        """Save name, xp and money into object."""
        self.name = name
        self.experience_level = experience_level
        self.money = money

    def __repr__(self):
        """Print output."""
        return f"Baker: {self.name}({self.experience_level})"


class Pastry:
    """Class for pastries."""

    def __init__(self, name: str, complexity_level: int):
        """Save name and complexity into object."""
        self.name = name
        self.complexity_level = complexity_level

    def __repr__(self):
        """Print output."""
        return f"{self.name}"


class Bakery:
    """Class for creating and managing a bakery."""

    def __init__(self, name: str, min_experience_level: int, budget: int):
        """Constructor, save name, min xp level and budget into obj. Also create assisting variables."""
        self.name = name
        self.min_experience_level = min_experience_level
        self.budget = budget
        self.bakers = []
        self.recipes = {}
        self.made_pastries = []

    def add_baker(self, baker: Baker) -> Baker or None:
        """Add baker to bakery if baker is a Baker class object and xp level is higher or equal to min xp level."""
        if type(baker) is Baker and baker.experience_level >= self.min_experience_level:
            self.bakers.append(baker)
            return baker
        return None

    def remove_baker(self, baker: Baker):
        """Remove baker from bakery if it's in the bakery."""
        if baker in self.bakers:
            self.bakers.remove(baker)

    def add_recipe(self, name: str):
        """Add new recipe to bakery if can afford and able to do so."""
        if len(name) <= self.budget and len(self.bakers) and name not in self.recipes.keys():
            self.budget -= len(name)
            weakest_baker_level = float("inf")
            for baker in self.bakers:
                if baker.experience_level < weakest_baker_level:
                    weakest_baker_level = baker.experience_level
            self.recipes[name] = abs(len(name) * len(self.bakers) - weakest_baker_level)

    def make_order(self, name: str) -> Pastry or None:
        """Fulfill order if possible and return new Pastry object, otherwise return None."""
        if name in self.recipes.keys():
            closest_baker = (None, float("inf"))
            for baker in self.bakers:
                if closest_baker[1] > baker.experience_level >= self.recipes[name]:
                    closest_baker = (baker, baker.experience_level)
            if closest_baker[0] is not None:
                closest_baker[0].experience_level += len(name)
                closest_baker[0].money += 2 * len(name)
                self.budget += 2 * len(name)
                self.min_experience_level += 1
                pastry = Pastry(name, self.recipes[name])
                self.made_pastries.append(pastry)
                return pastry
        return None

    def get_recipes(self) -> dict:
        """Return list of recipes as dict."""
        return self.recipes

    def get_pastries(self) -> list:
        """Return list of made pastries in complexity level's decreasing order."""
        return sorted(self.made_pastries, key=lambda x: x.complexity_level, reverse=True)

    def get_bakers(self) -> list:
        """Return list of bakers in decending xp level list."""
        return sorted(self.bakers, key=lambda x: x.experience_level, reverse=True)

    def __repr__(self):
        """Print output."""
        return f"Bakery {self.name}: {len(self.bakers)} baker(s)"
