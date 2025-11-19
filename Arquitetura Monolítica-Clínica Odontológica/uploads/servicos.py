# Contém as regras de negócio (operações principais)

from modelos import Paciente, Consulta
from datetime import datetime

class ServicoClinica:
    def __init__(self, repo):
        self.repo = repo

    # --- Pacientes ---

    def cadastrar_paciente(self, nome, tel, end, nasc, cpf):
        pacientes = self.repo.listar("pacientes")
        novo_id = len(pacientes) + 1

        p = Paciente(novo_id, nome, tel, end, nasc, cpf)
        self.repo.adicionar("pacientes", p.__dict__)
        return novo_id

    def listar_pacientes(self):
        return self.repo.listar("pacientes")

    def adicionar_prontuario(self, paciente_id, descricao):
        pacientes = self.repo.listar("pacientes")

        for p in pacientes:
            if p["id"] == paciente_id:
                p["historico"].append({
                    "data": datetime.now().strftime("%d/%m/%Y %H:%M"),
                    "descricao": descricao
                })
                self.repo.atualizar_lista("pacientes", pacientes)
                return True

        return False

    # --- Consultas ---

    def agendar_consulta(self, paciente_id, dentista, data, proc, valor):
        consultas = self.repo.listar("consultas")
        novo_id = len(consultas) + 1

        c = Consulta(novo_id, paciente_id, dentista, data, proc, valor)
        self.repo.adicionar("consultas", c.__dict__)
        return novo_id

    def listar_consultas(self):
        return self.repo.listar("consultas")

    def marcar_pagamento(self, consulta_id):
        consultas = self.repo.listar("consultas")

        for c in consultas:
            if c["id"] == consulta_id:
                c["pago"] = True
                self.repo.atualizar_lista("consultas", consultas)
                return True

        return False