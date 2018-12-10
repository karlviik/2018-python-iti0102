import requests
import random


class CannotAddPokemonException(Exception):
    """Custom exception."""
    pass


class NoAvailablePokemonsInWorldException(Exception):
    """Custom exception."""
    pass


class Person:
    """Simple Person class."""

    def __init__(self, name, age):
        """
        Person constructor.

        :param name: Name of the Person.
        :param age:  Age of the Person.
        """
        self.name = name
        self.age = age
        self.pokemon = None

    def add_pokemon(self, pokemon):
        """
        Add pokemon to Person.

        :param pokemon: Pokemon to add.
        :return:
        """
        if self.pokemon is None:
            if type(pokemon) is Pokemon:
                self.pokemon = pokemon
            else:
                raise CannotAddPokemonException("Must be instance of Pokemon!")
        else:
            raise CannotAddPokemonException("Person already has a pokemon!")

    def get_pokemon(self):
        """
        Get Person's Pokemon.

        :return: Pokemon or None.
        """
        return self.pokemon

    def remove_pokemon(self):
        """Remove Person's Pokemon."""
        self.pokemon = None

    def __repr__(self):
        """
        Representation of object.

        :return: Person's name, Person's age, Pokemon: Person's pokemon.
        """
        return f"{self.name}, {self.age}, Pokemon: {self.pokemon}"


class Data:
    """Class for getting data from API."""

    @staticmethod
    def get_all_pokemons_data(url):
        """
        Make request to API.

        :param endpoint: Address where to make the GET request.
        :return: Response data.
        """
        return requests.get(url).json()

    @staticmethod
    def get_additional_data(url):
        """
        Make request to API to get additional data for each Pokemon.

        :param endpoint: Address where to make the GET request.
        :return: Response data.
        """
        return requests.get(url).json()


class Pokemon:
    """Class for Pokemon."""

    def __init__(self, name, experience, attack, defence, types):
        """
        Class constructor.

        :param name: Pokemon's name.
        :param experience: Pokemon's experience
        :param attack: Pokemon's attack level
        :param defence: Pokemon's defence level.
        :param types: Pokemon's types.
        """
        self.name = name
        self.experience = experience
        self.attack = attack
        self.defence = defence
        self.types = types

    def get_power(self):
        """
        Calculate power of Pokemon.

        :return: Power.
        """
        return (self.experience / self.attack + self.defence) * len(self.name)

    def __str__(self):
        """
        String representation of object.

        :return: Pokemon's name, experience: Pokemon's experience, att: Pokemon's attack level, def: Pokemon's defence level, types: Pokemon's types.
        """
        return f"{self.name} experience: {self.experience} att: {self.attack} def: {self.defence} types: {self.types}"

    def __repr__(self):
        """
        Object representation.

        :return: Pokemon's name
        """
        return self.name


class World:
    """World class."""

    def __init__(self, name):
        """
        Class constructor.

        :param name:
        """
        self.name = name
        self.pokemons = []
        self.available_pokemons = []

    def add_pokemons(self, no_of_pokemons):
        """
        Add Pokemons to world, GET data from the API.
        """
        data = Data.get_all_pokemons_data("https://pokeapi.co/api/v2/pokemon/")
        for i in range(no_of_pokemons):
            url = data["results"][i]["url"]
            pokedata = Data.get_additional_data(url)

            name = pokedata["name"].upper()
            experience = pokedata["base_experience"]
            attack = pokedata["stats"][-2]["base_stat"]
            defence = pokedata["stats"][-3]["base_stat"]
            types = []
            for j in range(len(pokedata["types"])):
                types.append(pokedata["types"][j]["type"]["name"])
            pokemon = Pokemon(name, experience, attack, defence, types)
            self.pokemons.append(pokemon)
            self.available_pokemons.append(pokemon)

    def get_pokemons_by_type(self):
        """
        Get Pokemons by type.

        :return: Dict of Pokemons, grouped by types.
        """
        type_grouping = {}
        for pokemon in self.pokemons:
            for type in pokemon.types:
                if type not in type_grouping.keys():
                    type_grouping[type] = [pokemon]
                else:
                    type_grouping[type].append(pokemon)
        return type_grouping

    def hike(self, person: Person):
        """
        Person goes to a hike to find a Pokemon.

        :param person: Person who goes to hike.
        """
        if len(self.available_pokemons) == 0:
            raise NoAvailablePokemonsInWorldException("Could not find any pokemons.")
        else:
            pokemon = random.choice(self.available_pokemons)
            self.remove_available_pokemon(pokemon)
            person.add_pokemon(pokemon)

    def remove_available_pokemon(self, pokemon: Pokemon):
        """
        Remove Pokemon from available Pokemons, which means that the Pokemon got a owner.

        :param pokemon: Pokemon to be removed.
        """
        self.available_pokemons.remove(pokemon)

    def remove_pokemon_from_world(self, pokemon: Pokemon):
        """
        Remove Pokemon from the world, which means that the Pokemon died.

        :param pokemon: Pokemon to be removed.
        """
        self.pokemons.remove(pokemon)

    def fight(self, person1: Person, person2: Person):
        """
        Two people fight with their Pokemons.

        :param person1:
        :param person2:
        :return: Pokemon which wins.
        """
        poke1 = person1.pokemon
        poke2 = person2.pokemon
        if person1.pokemon.get_power() > person2.pokemon.get_power():
            winner = person1
            self.remove_pokemon_from_world(person2.pokemon)
            person2.remove_pokemon()
        else:
            winner = person2
            self.remove_pokemon_from_world(person1.pokemon)
            person1.remove_pokemon()
        return f"There was a battle between {poke1.name} and {poke2.name} and the winner was {winner.name}"

    def group_pokemons(self):
        """
        Group Pokemons by given format.

        :return: Dictionary of grouped Pokemons.
        """
        types = {"EARTH": ["poison", "grass", "bug", "ground", "rock"], "FIRE": ["fire", "electric"], "WATER": ["water", "ice"], "AIR": ["flying", "fairy", "ghost"], "OTHER": ["normal", "fighting", "psychic", "steel"]}
        grouped = {}
        for pokemon in self.pokemons:
            for mastertype, minortypes in types.items():
                if pokemon.types[0] in minortypes:
                    if mastertype in grouped.keys():
                        grouped[mastertype].append(pokemon)
                    else:
                        grouped[mastertype] = [pokemon]
                    continue
        return grouped

    def sort_by_type_experience(self):
        """
        Sort Pokemons by type adn experience. The first Pokemons should be Fire type and experience level of under 100.

        :return: List of sorted Pokemons.
        """
        pass

    def get_most_experienced_pokemon(self):
        """
        Get the Pokemon(s) which has the maximum experience level.
        """
        maxexp = 0
        maxpokes = []
        for pokemon in self.pokemons:
            if pokemon.experience > maxexp:
                maxexp = pokemon.experience
                maxpokes = [pokemon]
            elif pokemon.experience == maxexp:
                maxpokes.append(pokemon)
        return maxpokes

    def get_min_experience_pokemon(self):
        """
        Get the Pokemon(s) which has the minimum experience level.
        """
        minexp = float("inf")
        minpokes = []
        for pokemon in self.pokemons:
            if pokemon.experience < minexp:
                minexp = pokemon.experience
                minpokes = [pokemon]
            elif pokemon.experience == minexp:
                minpokes.append(pokemon)
        return minpokes


class Main:
    if __name__ == '__main__':
        world = World("Poke land")
        world.add_pokemons(10)
        print(len(world.pokemons))  # -> 128
        print(len(world.get_pokemons_by_type().keys()))  # -> 16
        ago = Person("Ago", 10)
        peeter = Person("Peeter", 11)
        print(len(world.available_pokemons))  # -> 128
        world.hike(ago)
        print(ago.pokemon.name)
        world.hike(peeter)
        print(peeter)
        print(len(world.available_pokemons))  # -> 126
        print(world.get_most_experienced_pokemon())  # -> [CHANSEY]
        print(world.get_min_experience_pokemon())  # -> [CATERPIE, WEEDLE]
        print(world.fight(ago, peeter))  # String that says who battled with who and who won.