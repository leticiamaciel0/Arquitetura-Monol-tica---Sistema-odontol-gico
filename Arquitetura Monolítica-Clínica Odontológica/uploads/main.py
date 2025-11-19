# Arquivo principal do sistema (ponto de entrada)

from repositorio import RepositorioJSON
from servicos import ServicoClinica
from interface import InterfaceConsole

def main():
    repo = RepositorioJSON("banco.json")  # banco local
    servico = ServicoClinica(repo)        # regras de negócio
    ui = InterfaceConsole(servico)        # interface do usuário
    ui.menu()                             # inicia o sistema

if __name__ == "__main__":
    main()