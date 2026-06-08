from aplicacao_clientes import SistemaClientes
from hash_sha1 import gerar_sha1


sistema = SistemaClientes()

sistema.carregar_dados(
    "dataset_clientes_transacoes.xlsx"
)

while True:

    print("\n===== MENU =====")
    print("1 - Buscar cliente")
    print("2 - Gerar SHA-1 do CPF")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        cpf = input("CPF: ")

        resultado = sistema.buscar_cliente(cpf)

        if resultado:

            print("\nCliente encontrado:")

            for transacao in resultado:

                print(transacao)

        else:

            print("Cliente não encontrado.")

    elif opcao == "2":

        cpf = input("CPF: ")

        print(
            gerar_sha1(cpf)
        )

    elif opcao == "3":

        print("Encerrando...")
        break