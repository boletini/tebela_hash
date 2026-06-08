import pandas as pd

from hash_encadeamento import HashEncadeamento


class SistemaClientes:

    def __init__(self):

        self.hash_clientes = HashEncadeamento(200)

    def carregar_dados(self, arquivo):

        df = pd.read_excel(arquivo)

        print("Registros originais:", len(df))

        df = df.drop_duplicates()

        print("Após deduplicação:", len(df))

        for _, linha in df.iterrows():

            cpf = str(linha["cpf"])

            dados = {
                "nome": linha["nome"],
                "data": linha["data_transacao"],
                "valor": linha["valor"]
            }

            existente = self.hash_clientes.buscar(cpf)

            if existente is None:

                self.hash_clientes.inserir(
                    cpf,
                    [dados]
                )

            else:

                existente.append(dados)

    def buscar_cliente(self, cpf):

        return self.hash_clientes.buscar(str(cpf))