
# Define as classes principais do sistema (modelo de domínio)

from datetime import datetime

class Paciente:
    def __init__(self, id, nome, telefone, endereco, data_nasc, cpf):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.data_nasc = data_nasc
        self.cpf = cpf
        self.historico = []  # lista de registros clínicos


class ProntuarioItem:
    def __init__(self, data, descricao):
        self.data = data
        self.descricao = descricao


class Consulta:
    def __init__(self, id, paciente_id, dentista, data_horario, procedimento, valor):
        self.id = id
        self.paciente_id = paciente_id
        self.dentista = dentista
        self.data_horario = data_horario
        self.procedimento = procedimento
        self.valor = valor
        self.pago = False  # pagamento pendente


class Usuario:
    def __init__(self, username, senha, perfil):
        self.username = username
        self.senha = senha
        self.perfil = perfil