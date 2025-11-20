from repositorio import RepositorioJSON
from servicos import ServicoClinica
from interface import InterfaceConsole

def main():
    repo = RepositorioJSON("banco.json")
    servico = ServicoClinica(repo)
    ui = InterfaceConsole(servico)
    ui.iniciar()

if __name__ == "__main__":
    main()