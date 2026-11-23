import src.utils as utils


def app():
    controle = True
    escolha = None
    bot = None
    alternativas = [
        "Deseja coletar livros",
        "Deseja ver coleções de livros",
        "Deseja limpar coleções de livros",
        "Deseja encerrar o programa",
    ]
    alternativasExcepcao = ["Deseja continuar o programa", "Deseja encerrar o programa"]

    utils.limparTerminal()
    while controle:
        try:
            print("Seja muito bem-vindo ao Bot-Livros")
            print("-" * 50)
            utils.exibirAlternativas(*alternativas)
            escolha = int(input("Digite um número das alternativas: "))
            while escolha not in list(range(len(alternativas))):
                escolha = int(input("Digite o número da alternativa: "))
            match escolha:
                case 1:
                    livros = {}
                    entradaCategoria = input("Digite uma categoria literária: ")
                    entradaQuantLivros = int(input("Digite a quantidade de livros: "))

                    if (
                        entradaCategoria == ""
                        or entradaCategoria.isalnum()
                        or entradaCategoria.isnumeric()
                    ):
                        raise ValueError(
                            "Precisamos de uma categoria literário! Tente Novamente."
                        )
                    if entradaQuantLivros <= 0:
                        raise ValueError(
                            "Precisamos de uma quantidade maior que zero (0)! Tente Novamente."
                        )

                case 2:
                    ...
                case 3:
                    ...
                case 4:
                    controle = False
                    break
        except TypeError as erro:
            utils.limparTerminal()
            print(erro)
        except ValueError as erro:
            utils.limparTerminal()
            print(erro)
        finally:
            ...


if __name__ == "__main__":
    app()
