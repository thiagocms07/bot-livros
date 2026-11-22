import subprocess
from platform import system
from colorama import init, deinit
from colorama.ansi import Fore, Style

def exibirAlternativas(*alternativas: str) -> None:
    if len(alternativas) == 0 or len(alternativas) == 1:
        raise ValueError("Essa função precisa de pelo menos dois (2) valores")

    verificacaoAlternativa = lambda x: isinstance(x, str) and x != ""
    alternativasFiltradas = enumerate(filter(verificacaoAlternativa, alternativas), start=1)
    modeloAlternativa = "[{}] - {}"

    init()
    for indice, alternativa in alternativasFiltradas:
        print(modeloAlternativa.format(
            Fore.GREEN + str(indice) + Style.RESET_ALL, 
            Fore.CYAN + alternativa + Style.RESET_ALL))
    deinit()
    
def limparTerminal() -> None:
    comando = 'cls' if system().lower() == "windows" else 'clear'
    subprocess.run(comando, shell=True)

if __name__ == '__main__': 
    limparTerminal()
    exibirAlternativas('oi', 2, 'olá', '')