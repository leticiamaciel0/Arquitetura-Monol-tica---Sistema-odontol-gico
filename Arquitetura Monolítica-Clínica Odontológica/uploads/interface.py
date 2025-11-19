# Interface de console (menu e entradas do usuário)

class InterfaceConsole:
    def __init__(self, servico):
        self.s = servico

    def menu(self):
        while True:
            print("\n=== Sistema da Clínica Odontológica ===")
            print("1 - Cadastrar Paciente")
            print("2 - Listar Pacientes")
            print("3 - Adicionar Prontuário")
            print("4 - Agendar Consulta")
            print("5 - Listar Consultas")
            print("6 - Marcar Pagamento")
            print("0 - Sair")

            op = input("Escolha: ")

            if op == "1":
                self.cadastrar_paciente()
            elif op == "2":
                self.listar_pacientes()
            elif op == "3":
                self.adicionar_prontuario()
            elif op == "4":
                self.agendar_consulta()
            elif op == "5":
                self.listar_consultas()
            elif op == "6":
                self.marcar_pagamento()
            elif op == "0":
                break

    # --- Telas individuais ---

    def cadastrar_paciente(self):
        nome = input("Nome: ")
        tel = input("Telefone: ")
        end = input("Endereço: ")
        nasc = input("Data de nascimento: ")
        cpf = input("CPF: ")

        pid = self.s.cadastrar_paciente(nome, tel, end, nasc, cpf)
        print(f"Paciente cadastrado com ID {pid}")

    def listar_pacientes(self):
        print("\n--- Pacientes ---")
        for p in self.s.listar_pacientes():
            print(f"{p['id']} - {p['nome']} - CPF: {p['cpf']}")

    def adicionar_prontuario(self):
        pid = int(input("ID do paciente: "))
        desc = input("Descrição: ")

        if self.s.adicionar_prontuario(pid, desc):
            print("Registro adicionado!")
        else:
            print("Paciente não encontrado.")

    def agendar_consulta(self):
        pid = int(input("ID Paciente: "))
        dent = input("Dentista: ")
        data = input("Data/Hora: ")
        proc = input("Procedimento: ")
        valor = float(input("Valor: "))

        cid = self.s.agendar_consulta(pid, dent, data, proc, valor)
        print(f"Consulta agendada com ID {cid}")

    def listar_consultas(self):
        print("\n--- Consultas ---")
        for c in self.s.listar_consultas():
            pago = "Sim" if c["pago"] else "Não"
            print(f"{c['id']} - Paciente {c['paciente_id']} - {c['procedimento']} - R$ {c['valor']} - Pago: {pago}")

    def marcar_pagamento(self):
        cid = int(input("ID da consulta: "))
        if self.s.marcar_pagamento(cid):
            print("Pagamento registrado!")
        else:
            print("Consulta não encontrada.")