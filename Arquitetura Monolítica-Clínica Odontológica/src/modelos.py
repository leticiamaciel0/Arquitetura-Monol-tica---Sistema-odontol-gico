# Entidades de domínio simples

from datetime import datetime

class Usuario:
    def __init__(self, id, username, senha_hash, role):
        self.id = id
        self.username = username
        self.senha_hash = senha_hash
        self.role = role  # 'secretaria'|'dentista'|'paciente'

    def to_dict(self):
        return {"id": self.id, "username": self.username, "senha_hash": self.senha_hash, "role": self.role}


class Paciente:
    def __init__(self, id, nome, telefone, endereco, data_nasc, cpf, user_id=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.user_id = user_id
        self.historico = []  # lista de {data, texto, autor}

    def to_dict(self):
        return {
            "id": self.id, "nome": self.nome, "telefone": self.telefone,
            "endereco": self.endereco, "data_nasc": self.data_nasc,
            "cpf": self.cpf, "user_id": self.user_id, "historico": self.historico
        }


class Consulta:
    def __init__(self, id, paciente_id, dentista, data_horario, procedimento, valor):
        self.id = id
        self.paciente_id = paciente_id
        self.dentista = dentista
        self.data_horario = data_horario  # string "YYYY-MM-DD HH:MM"
        self.procedimento = procedimento
        self.valor = valor
        self.status = "agendada"
        self.pago = False

    def to_dict(self):
        return {
            "id": self.id, "paciente_id": self.paciente_id, "dentista": self.dentista,
            "data_horario": self.data_horario, "procedimento": self.procedimento,
            "valor": self.valor, "status": self.status, "pago": self.pago
        }