import random

def heads_or_tails_game():
    name = input("Who are you?\n> ")
    print(f"Hello, {name}")
    
    print("Tossing a coin...")

    results = []
    for i in range(1, 4):
        result = random.choice(['Heads', 'Tails'])
        results.append(result)
        print(f"Round {i}: {result}")

    heads_count = results.count('Heads')
    tails_count = results.count('Tails')
    print(f"Heads: {heads_count}, Tails: {tails_count}")

    if heads_count > tails_count:
        print(f"{name} won!")
    else:
        print(f"{name} lost!")

if __name__ == "__main__":
    heads_or_tails_game()
