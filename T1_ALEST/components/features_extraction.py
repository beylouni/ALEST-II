import re

def extract(file):
    """
        Args: 
            Arquivo txt contendo as informações sobre o jogo
        Return:
            int com o número de rodadas,
            dicionário de dicionário contendo {idmacaco : {'par': n, 'impar': n, 'pedrinhas': [n, n, n, n, ...]}}
    """
    #Expressões regulares
    regex_rounds = r'Fazer (\d+) rodadas'
    regex_mounkeys = r'Macaco (\d+) par -> (\d+) impar -> (\d+) : \d+ :\s+(.+)'

    rounds = 0
    info_mounkeys = {}

    with open(file, 'r') as f:
        text = f.read()

    #Extraindo o número de rodadas
    match_rounds = re.search(regex_rounds, text)
    if match_rounds:
        rounds = int(match_rounds.group(1))

    #Extraindo as informações sobre cada macaco
    for match_mounkey in re.finditer(regex_mounkeys, text):
        mounkey = int(match_mounkey.group(1))
        even = int(match_mounkey.group(2))
        odd = int(match_mounkey.group(3))
        stones = match_mounkey.group(4)

        if stones:
            stones = list(map(int, stones.split()))
        else:
            stones = []
        info_mounkeys[mounkey] = {'id': mounkey ,'even': even, 'odd': odd, 'stones': stones}
    
    return rounds, info_mounkeys

def even_or_odd(number):
    """
        -Alterar para regex depois-
        Args: 
            Número para checar se é par ou impar
        Return:
            True  = Even
            False = Odd
    """
    if number % 2 == 0:
        return True
    return False
