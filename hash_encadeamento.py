class HashEncadeamento:

    def __init__(self, tamanho=100):

        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def hash(self, chave):
        return int(chave) % self.tamanho

    def inserir(self, chave, valor):

        indice = self.hash(chave)

        self.tabela[indice].append((chave, valor))

    def buscar(self, chave):

        indice = self.hash(chave)

        for k, valor in self.tabela[indice]:

            if k == chave:
                return valor

        return None

    def mostrar(self):

        for i, lista in enumerate(self.tabela):

            if lista:
                print(i, lista)