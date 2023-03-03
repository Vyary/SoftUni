from project.pokemon import Pokemon  # for judge system
# from pokemon import Pokemon


class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemons:
            return "This pokemon is already caught"

        self.pokemons.append(pokemon)
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name):
        try:
            match = next(filter(lambda x: x.name == pokemon_name, self.pokemons))
            self.pokemons.remove(match)
            return f"You have released {pokemon_name}"
        except StopIteration:
            return "Pokemon is not caught"

    def trainer_data(self):
        pokemon_data = "\n".join(
            f"- {pokemon.pokemon_details()}" for pokemon in self.pokemons
        )
        return (
            f"Pokemon Trainer {self.name}\n"
            + f"Pokemon count {len(self.pokemons)}\n"
            + f"{pokemon_data}"
        )
