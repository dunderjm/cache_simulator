import math

class Cache:
    def __init__(self, n_linhas):
        self.n_linhas = n_linhas
        self.n_bits = int(math.log(n_linhas, 2))
        tabela = [0, '', ''] #[V, TAG, DADOS]
        lista = [(i, tabela[:]) for i in range(n_linhas)]
        self.cache = {key: value for key, value in lista}
        self.miss = 0
        self.hit = 0
                  

    def consulta(self, adress):
        adress_cache = int(adress[-self.n_bits:], 2)
        tag = adress[:len(adress) - self.n_bits]
        if tag == self.cache[adress_cache][1] and self.cache[adress_cache][0] == 1:
            self.hit += 1
        else:
            self.cache[adress_cache][0] = 1
            self.cache[adress_cache][1] = tag
            self.cache[adress_cache][2] = adress
            self.miss += 1
            
