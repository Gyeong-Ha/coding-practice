import sys

input = sys.stdin.read


def main():
    data = input().splitlines()

    # Divide inputs into pokemon list and problems
    num_poke, num_q = map(int, data[0].split())
    pokemons = data[1 : num_poke + 1]

    # Create a dictionary for quick name to index lookup
    poke_dict = {name: idx + 1 for idx, name in enumerate(pokemons)}

    output = []
    for q in data[num_poke + 1 :]:
        if q.isdigit():  # Pokemon Idx?
            output.append(pokemons[int(q) - 1])
        else:  # Pokemon Name?
            output.append(str(poke_dict[q]))

    # Print all results at once to minimize I/O operations
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()