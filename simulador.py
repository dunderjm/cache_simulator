import math
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
        enderecos = input().split()
    except ValueError:
        print('Uma das entradas não é base 2')
    else:
        for i in enderecos:
            cache.consulta(i)
        print(f'Hit: {cache.hit}')
        print(f'Miss:{cache.miss}')

main()