from collections import namedtuple


def parse_game_info(file_path):

    num_rounds = 0
    monkeys = {}

    with open(file_path, 'r') as f:
        text = f.read()
    
    rodadas = text.split()[1]
    print(rodadas)

    for line in text:
        infos = []
        id = list(line)
        infos = infos.append(id)
        print(infos)

    return num_rounds, monkeys


def distribute_coconuts(monkeys, coconuts, even_dest, odd_dest):
    while coconuts:
        coconut = coconuts.pop(0)
        if (lambda num: num % 2 == 0)(coconut):
            monkeys[even_dest]['coconuts'].append(coconut)
        else:
            monkeys[odd_dest]['coconuts'].append(coconut)


def get_winner(monkeys):
    max_coconuts = -1
    winner_id = -1
    for monkey_id, monkey_data in monkeys.items():
        num_coconuts = len(monkey_data['coconuts'])
        if num_coconuts > max_coconuts:
            max_coconuts = num_coconuts
            winner_id = monkey_id
    return winner_id


def play_game(file_path):
    num_rounds, monkey_data = parse_game_info(file_path)

    Monkey = namedtuple('Monkey', ['id', 'even_dest', 'odd_dest', 'coconuts'])
    monkeys = {monkey_id: Monkey(monkey_id, data['even'], data['odd'], data['coconuts'])
               for monkey_id, data in monkey_data.items()}

    for _ in range(num_rounds):
        for monkey in monkeys.values():
            coconuts = monkey.coconuts
            even_dest = monkey.even_dest
            odd_dest = monkey.odd_dest
            monkeys[monkey.id] = Monkey(monkey.id, even_dest, odd_dest, [])
            distribute_coconuts(monkeys, coconuts, even_dest, odd_dest)

    for monkey in monkeys.values():
        print(f'Monkey {monkey.id} has coconuts: {monkey.coconuts}')

    print(f'The winning monkey is monkey {get_winner(monkeys)}')


parse_game_info(r'C:\Users\LucianoBeylouni\Downloads\T1_ALEST\T1_ALEST\arquivo.txt')

# if __name__ == '__main__':
#     play_game(r'C:\Users\LucianoBeylouni\Downloads\T1_ALEST\T1_ALEST\arquivo.txt')
