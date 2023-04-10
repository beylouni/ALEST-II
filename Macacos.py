import re
import time

class Macaco:
    def __init__(self, id, par, impar, cocos):
        self.id = id
        self.par = par
        self.impar = impar
        self.cocos = cocos

    def send_coco(self, coco):
        if coco % 2 == 0:
            destinatario.receive_coco(self.par)
        else:
            destinatario.receive_coco(self.impar)

    def receive_coco(self, coco):
        self.cocos.append(coco)

class Jogo:
    def __init__(self, file_path):
        rodadas, infos = self.extract(file_path)
        self.rodadas = rodadas
        self.macaco = [Macaco(m['id'], m['par'], m['impar'], m['cocos']) for m in infos.values()]

    def extract(self, file_path):
        rodadas_r = r'Fazer (\d+) rodadas'
        macaco_r = r'Macaco (\d+) par -> (\d+) impar -> (\d+) : (\d+) :\s*(.*)'
        rodadas = 0
        infos = {}

        with open(file_path, 'r') as f:
            text = f.read()

        match_rodadas = re.search(rodadas_r, text)
        if match_rodadas:
            rodadas = int(match_rodadas.group(1))

        for match_monkey in re.finditer(macaco_r, text):
            monkey = int(match_monkey.group(1))
            par = int(match_monkey.group(2))
            impar = int(match_monkey.group(3))
            cocos_str = match_monkey.group(5)
            cocos = []
            if cocos_str:
                cocos = [int(x) for x in re.findall(r'\d+', cocos_str)]
                cocos = list(map(int, cocos))
            else:
                cocos = []
            infos[monkey] = {'id': monkey ,'par': par, 'impar': impar, 'cocos': cocos}
        return rodadas, infos

    def play_round(self):
        for i, remetente in enumerate(self.macaco):
            remetente_cocos = remetente.cocos
            for coco in remetente_cocos:
                destinatario = self.macaco[remetente.par if coco % 2 == 0 else remetente.impar]
                destinatario.cocos.append(coco)
            remetente_cocos.clear()
        # for i in range(len(self.macaco)):
        #     remetente = self.macaco[i]
        #     for j in range(len(remetente.cocos)):
        #         coco = remetente.cocos[j]
        #         if coco % 2 == 0:
        #             destinatario = self.macaco[remetente.par]
        #             destinatario.cocos.append(coco)
        #         else:
        #             destinatario = self.macaco[remetente.impar]
        #             destinatario.cocos.append(coco)
        #     remetente.cocos.clear()
    
    def get_winner(self):
        winner = max(self.macaco, key=lambda monkey: len(monkey.cocos))
        return winner.id

# Uso de caso

start_time = time.time()

bingo = Jogo(r"C:\Users\LucianoBeylouni\Downloads\T1_ALEST\casos_t1_2023_1\caso00.txt")
list(map(lambda x: bingo.play_round(), range(bingo.rodadas)))
print(f"O vencedor do jogo é o Macaco número {bingo.get_winner()}")

elapsed_time = time.time() - start_time

print(f"Elapsed time: {elapsed_time} seconds")