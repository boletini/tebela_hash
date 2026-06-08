class TabelaHash:

    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho

    def funcao_hash(self, chave):
        return int(chave) % self.tamanho

    def inserir(self, chave, valor):

        indice = self.funcao_hash(chave)

        if self.tabela[indice] is not None:
            print(f"COLISÃO na posição {indice}")

        self.tabela[indice] = valor

    def buscar(self, chave):

        indice = self.funcao_hash(chave)

        return self.tabela[indice]

    def mostrar(self):

        for i, item in enumerate(self.tabela):
            print(i, item)