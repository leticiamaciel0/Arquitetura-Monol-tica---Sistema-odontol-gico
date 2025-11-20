class InterfaceConsole:
    """Menus e interação com o usuário."""

    def __init__(self, servico):
        self.servico = servico

    # ------------------- INÍCIO -------------------
    def iniciar(self):
        while True:
            print("\n=== SELECIONE O TIPO DE USUÁRIO ===")
            print("1 - Secretaria")
            print("2 - Dentista")
            print("3 - Paciente")
            print("0 - Sair")

            escolha = input("Escolha: ")

            if escolha == "0":
                print("Saindo do sistema...")
                break

            tipos = {
                "1": "secretaria",
                "2": "dentista",
                "3": "paciente"
            }

            if escolha not in tipos:
                print("Opção inválida!")
                continue

            tipo_selecionado = tipos[escolha]
            print(f"\n=== LOGIN ({tipo_selecionado.upper()}) ===")

            login = input("Login: ")
            senha = input("Senha: ")

            usuario = self.servico.login(login, senha)

            if usuario and usuario["tipo"] == tipo_selecionado:
                print(f"\nBem-vindo, {usuario['tipo']}!\n")

                if usuario["tipo"] == "secretaria":
                    self.menu_secretaria()
                elif usuario["tipo"] == "dentista":
                    self.menu_dentista()
                elif usuario["tipo"] == "paciente":
                    self.menu_paciente(usuario)

            else:
                print("\n❌ Login inválido ou tipo incorreto!\n")

    # ------------------- MENU SECRETARIA -------------------
    def menu_secretaria(self):
        while True:
            print("\n--- MENU SECRETARIA ---")
            print("1 - Cadastrar Paciente")
            print("2 - Listar Pacientes")
            print("3 - Agendar Consulta")
            print("0 - Sair")

            op = input("Escolha: ")

            if op == "1":
                nome = input("Nome: ")
                cpf = input("CPF: ")
                self.servico.cadastrar_paciente(nome, cpf)
                print("Paciente cadastrado!")

            elif op == "2":
                for p in self.servico.listar_pacientes():
                    print(f"- {p['nome']} (CPF: {p['cpf']})")

            elif op == "3":
                paciente = input("Paciente: ")
                data = input("Data: ")
                dentista = input("Dentista: ")
                self.servico.agendar_consulta(paciente, data, dentista)
                print("Consulta agendada!")

            elif op == "0":
                print("Voltando ao login...")
                return

            else:
                print("Opção inválida!")

    # ------------------- MENU DENTISTA -------------------
    def menu_dentista(self):
        while True:
            print("\n--- MENU DENTISTA ---")
            print("1 - Ver Consultas")
            print("0 - Sair")

            op = input("Escolha: ")

            if op == "1":
                for c in self.servico.listar_consultas():
                    print(f"{c['data']} - {c['paciente']} (Dentista: {c['dentista']})")

            elif op == "0":
                print("Voltando ao login...")
                return

            else:
                print("Opção inválida!")

    # ------------------- MENU PACIENTE -------------------
    def menu_paciente(self, usuario):
        while True:
            print("\n--- MENU PACIENTE ---")
            print("1 - Minhas Consultas")
            print("0 - Sair")

            op = input("Escolha: ")

            if op == "1":
                consultas = self.servico.listar_consultas_paciente(usuario["login"])
                for c in consultas:
                    print(f"{c['data']} - Dentista: {c['dentista']}")

            elif op == "0":
                print("Voltando ao login...")
                return

            else:
                print("Opção inválida!")