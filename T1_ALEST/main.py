from components.features_extraction import extract
from components.Monkey import Monkey
from components.game import travel, winner

rounds, info_mounkeys = extract('arquivo3.txt')
monkeys = []

for i in range(len(info_mounkeys)):
    monkey = Monkey(info_mounkeys[i]['id'], info_mounkeys[i]['even'], info_mounkeys[i]['odd'], info_mounkeys[i]['stones'])
    monkeys.append(monkey)

for _ in range(rounds):
    for k in range(len(monkeys)):
        coconuts = monkeys[k].get_coconuts()
        even = monkeys[k].get_even_destination()
        odd = monkeys[k].get_odd_destination()
        #Como já armazenamos todos os cocos do macaco atual na variavel coconuts, zeramos o atributo coconuts do macaco(como se ele já tivesse enviado todos seus cocos)
        monkeys[k].reset_coconuts()
        travel(monkeys, coconuts, even, odd)

#Somente testando se o algoritmo está distribuindo os cocos corretamente
for i in range(len(monkeys)):
    print(f'Macaco : {monkeys[i].get_id()}')
    print(f'Cocos: {monkeys[i].get_coconuts()}')

print(f'O macaco vencedor e o numero: {winner(monkeys)}')
