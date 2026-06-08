class HashLinear:

    def __init__(self, tamanho=2000):

        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def hash(self, chave):
        return int(chave) % self.tamanho

    def inserir(self, chave, valor):

        indice = self.hash(chave)

        while self.tabela[indice] is not None:

            indice = (indice + 1) % self.tamanho

        self.tabela[indice] = (chave, valor)

    def buscar(self, chave):

        indice = self.hash(chave)

        while self.tabela[indice] is not None:

            k, valor = self.tabela[indice]

            if k == chave:
                return valor

            indice = (indice + 1) % self.tamanho

        return None