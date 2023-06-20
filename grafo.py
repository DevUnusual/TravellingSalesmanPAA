class Grafo():
    def __init__(self):
        self.grafo = {}
        self.inf = set()

    def __str__(self):
        visu = ''
        caminho = ''
        for k in self.grafo.keys():
            visu += f'{k:6}'
            for key, custo in self.grafo[k].items():
                caminho += f'--[{custo}]-->{key:->6}'
            visu += caminho + '\n'
            caminho = ''
        return visu

    def addNo(self, no: str, vizinhos: dict):
        ex = self.exist(no)  # verifica se o no existe
        for k, c in vizinhos.items():  # para toda key custo in vizinhos
            # verificar se ja faz parte das keys do no, caso ele ja tenha sido adicionado como vizinho
            if ex and k in self.grafo[no].keys():
                if self.grafo[no][k] != c:  # se o custo estiver diferente, atualiza
                    self.grafo[no][k] = c
                    self.grafo[k][no] = c
            elif ex and k in self.grafo.keys():  # caso o no exista e k ja possui alguma conexao
                self.grafo[no].update({k: c})
                self.grafo[k].update({no: c})
            elif ex:  # caso o no exista e k nao encontrado
                self.grafo[no].update({k: c})
                self.grafo[k] = {no: c}
            else:  # caso o no nao exista
                self.grafo[no] = vizinhos
                for key, custo in vizinhos.items():
                    self.addNo(key, {no: custo})
                break

    def normalize(self):
        keys = set(self.keys())
        for i in keys:
            keys_target = keys.difference(set(self.grafo[i].keys()))
            for k in keys_target:
                if i == k:
                    continue
                self.grafo[i].update({k: -1})
                self.grafo[k].update({i: -1})
                self.inf.add((i, k))

    def getValue(self, key1, key2):
        return self.grafo[key1][key2]

    def keys(self):
        return self.grafo.keys()

    def viewGraph(self):
        return self.grafo

    def exist(self, key):
        if key in self.grafo.keys():
            return True
        return False


if (__name__ == '__main__'):
    gra = Grafo()
    gra.addNo('carlo', {'biel': 2, 'paulo': 5})
    gra.addNo('biel', {'paulo': 3, 'pedro': 6, 'ams': 1})
    gra.normalize()
    print(gra.viewGraph())
    print(gra)
