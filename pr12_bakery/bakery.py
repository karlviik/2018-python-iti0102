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


if __name__ == '__main__':

    bakery1 = Bakery("Pagariposid", 10, 100)
    print(bakery1)  # Bakery Pagariposid: 0 baker(s)

    bakery1.add_baker(Baker("Ago", 9, 0))
    print(bakery1)  # Bakery Pagariposid: 0 baker(s) => Baker Ago was not added because of low experience level (Sorry Ago)

    print(bakery1.make_order("cake"))  # None => No such recipe nor baker in bakery

    ########################################################################

    polly = Baker("Polly", 10, 5)
    sam = Baker("Sam", 11, 0)
    emma = Baker("Emma", 12, 6)

    bakery1.add_baker(polly)
    bakery1.add_baker(sam)
    bakery1.add_baker(emma)

    # Trying to make order when no recipes are in bakery

    print(bakery1.make_order("cake"))  # None

    bakery1.add_recipe("cake")
    print(bakery1.budget)  # 96 (100 - len('cake') = 96 => price for recipe)
    print(bakery1.get_recipes())  # {'cake': 2}

    print(bakery1.make_order("cake"))  # cake
    print(
        bakery1.get_bakers())  # [Baker: Polly(14), Baker: Emma(12), Baker: Sam(11)] =>
    # Polly was chosen to be the baker because 'cake' complexity and Polly experience lever were the closest
    # Polly experience level was increased by len('cake') => 10 + 4 = 14

    print(bakery1.budget)  # 104 (used to be 96: 96 + len('cake') * 2 = 104)
    print(polly.money)  # 13 (5 she had + len('cake') * 2 = 13)

    print(bakery1.get_pastries())  # [cake] ("NB! cake is instance of class Pastry, not a string)

    ########################################################################

    bakery2 = Bakery("Pihlaka", 11, 100)

    john = Baker("John", 11, 5)
    megane = Baker("Megane", 17, 4)
    kate = Baker("Megane", 18, 8)

    bakery2.add_baker(john)
    bakery2.add_baker(megane)
    bakery2.add_baker(kate)


    bakery2.add_recipe("muffin")
    bakery2.add_recipe("cupcake")
    bakery2.add_recipe("biscuits")

    print(bakery2.get_recipes())  # {'muffin': 7, 'cupcake': 10, 'biscuits': 13}

    print(
        bakery2.get_bakers())  # [Baker: Megane(18), Baker: Megane(17), Baker: John(11)]
    bakery2.make_order("biscuits")
    print(
        bakery2.get_bakers())  # [Baker: Megane(25), Baker: Megane(18), Baker: John(11)]
    # Magane was chosen to be the baker as the most closest experience (which is also greater than complexity) was 17.
