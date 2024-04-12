import sys


n, m = map(int, sys.stdin.readline().strip().split())


class Pokemon:
    def __init__(self, number, name):
        self.number = number
        self.name = name


pokemon_dict = {}
for number in range(1, n + 1):
    name = sys.stdin.readline().strip()
    pokemon = Pokemon(number, name)

    pokemon_dict[name] = pokemon
    pokemon_dict[number] = pokemon


def find_pokemon(arg):
    return pokemon_dict[arg]


for _ in range(m):
    arg = sys.stdin.readline().strip()

    if arg.isdigit():
        pokemon = find_pokemon(int(arg))
        print(pokemon.name)
    else:
        pokemon = find_pokemon(arg)
        print(pokemon.number)
