import math
from collections import OrderedDict
class Cache:
    def __init__(self, n_linhas):
        self.n_linhas = n_linhas
        self.n_bits = int(math.log(n_linhas, 2))
        tabela = {'V': 0, 'Tag': '', 'Dados': ''}
        self.cache = [dict(tabela) for i in range(self.n_linhas)]
        self.miss = 0
        self.hit = 0
                  

    def consulta(self, adress):
        adress_cache = int(adress[-self.n_bits:], 2)
        tag = adress[:len(adress) - self.n_bits]
        if tag == self.cache[adress_cache]['Tag'] and self.cache[adress_cache]['V'] == 1:
            self.hit += 1
            return True
        else:
            self.cache[adress_cache]['V'] = 1
            self.cache[adress_cache]['Tag'] = tag
            self.cache[adress_cache]['Dados'] = adress
            self.miss += 1
            return False
