class Macaco():
    def __init__(self, id, par, impar, coco):
        self.id = id
        self.par = par
        self.impar = impar
        self.coco = coco

    def get_id(self):
        return self.id
    
    def get_par(self):
        return self.par
    
    def get_impar(self):
        return self.impar
    
    def get_coco(self):
        return self.coco
    
    def add_coco(self, cocos):
        self.coco += [cocos]

    def zera_coco(self):
        self.coco = []


def getRodadas(arq: str) -> int:
    with open(arq, 'r') as f:
        rodadas = f.readline().split()[1]
    print(rodadas)

    return rodadas


def getId(arq: str) -> int:
    with open(arq, 'r') as f:
        id = f.readlines()
    print(id)

    return id


getId(r'C:\Users\LucianoBeylouni\Downloads\T1_ALEST\T1_ALEST\arquivo.txt')

