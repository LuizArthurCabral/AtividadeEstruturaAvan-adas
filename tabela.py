class Tabela:
    def __init__(self, gavetas=8):
        self.gavetas = [[] for _ in range(gavetas)]
        self.tamanho = 0

    def posicao(self, chave):
        return hash(chave) % len(self.gavetas)

    def inserir(self, chave, valor):
        gaveta = self.gavetas[self.posicao(chave)]
        for i, (k, _) in enumerate(gaveta):
            if k == chave:
                gaveta[i] = (chave, valor)   # chave já existe: troca o valor
                return
        gaveta.append((chave, valor))
        self.tamanho += 1
        if self.tamanho / len(self.gavetas) > 0.75:
            self.crescer()

    def buscar(self, chave):
        for k, v in self.gavetas[self.posicao(chave)]:
            if k == chave:
                return v
        return None

    def remover(self, chave):
        gaveta = self.gavetas[self.posicao(chave)]
        for i, (k, _) in enumerate(gaveta):
            if k == chave:
                del gaveta[i]
                self.tamanho -= 1
                return True
        return False

    def crescer(self):
        antigas = self.gavetas
        self.gavetas = [[] for _ in range(2 * len(antigas))]
        for gaveta in antigas:
            for k, v in gaveta:
                # refaz a conta com o novo divisor, não copia a gaveta
                self.gavetas[self.posicao(k)].append((k, v))