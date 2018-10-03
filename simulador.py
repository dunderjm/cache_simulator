import math
import pandas as pd
from cache import Cache

def filtro_base_2(entrada):
    n = math.log(entrada, 2)
    if not n //1 == n:
        raise ValueError('Número não é base 2')

def main():
    try:
        linha_cache = int(input('Número de linhas da Memória Cache: '))
        linha_MP = int(input('Número de linhas da Memória Principal: '))
        filtro_base_2(linha_cache)
        filtro_base_2(linha_MP)
        cache = Cache(linha_cache)
    except ValueError:
        print('Uma das entradas não está na base 2')
    else:
        while(True):
            adress = input('Digite o endereço ou 0 para sair: ')
            if adress != '0':
                if(cache.consulta(adress)):
                    print('Hit')
                else:
                    print('Miss')
            else:
                break   
        tabela = pd.DataFrame(cache.cache)
        tabela = tabela[['V', 'Tag', 'Dados']]
        print(tabela)
        print(f'Numero total de Hit: {cache.hit}')
        print(f'Numero total de Miss:{cache.miss}')

main()