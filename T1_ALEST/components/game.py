from components.features_extraction import even_or_odd

def travel(monkeys, coconuts, even_destination, odd_destination):
    """
        Args: 
            lista de cocos, indice do macaco destino quando é par, indice do macaco destino quando é impar
        Return:
            None, altera as listas inplace
    """
    while(len(coconuts) > 0):
        aux = coconuts.pop(0)
        if even_or_odd(aux):
            monkeys[even_destination].add_coconut(aux)
        else:
            monkeys[odd_destination].add_coconut(aux)

def winner(monkeys):
    """
        Args: 
            Lista de macacos
        Return:
            Id do macaco ganhador
    """
    winner = monkeys[0].get_id()
    for i in range(len(monkeys)):
        if (len(monkeys[i].get_coconuts()) > len(monkeys[winner].get_coconuts())):
            winner = monkeys[i].get_id()
    return winner