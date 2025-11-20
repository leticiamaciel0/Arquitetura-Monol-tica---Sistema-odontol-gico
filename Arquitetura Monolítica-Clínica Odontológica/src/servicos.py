class ServicoClinica:
    """Regras de negócio do sistema."""

    def __init__(self, repo):
        self.repo = repo
        self._criar_usuarios_iniciais()

    # Cria contas iniciais apenas 1 vez
    def _criar_usuarios_iniciais(self):
        usuarios = self.repo.listar_usuarios()
        if usuarios:
            return

        # Usuários padrão
        self.repo.salvar_usuario({"login": "b", "senha": "123", "tipo": "secretaria"})
        self.repo.salvar_usuario({"login": "d", "senha": "123", "tipo": "dentista"})
        
        # Para testar paciente
        self.repo.salvar_usuario({"login": "c", "senha": "123", "tipo": "paciente"})

    # LOGIN
    def login(self, login, senha):
        for u in self.repo.listar_usuarios():
            if u["login"] == login and u["senha"] == senha:
                return u
        return None

    # SECRETARIA
    def cadastrar_paciente(self, nome, cpf):
        paciente = {"nome": nome, "cpf": cpf}
        self.repo.salvar_paciente(paciente)
        return True

    def listar_pacientes(self):
        return self.repo.listar_pacientes()

    # CONSULTAS
    def agendar_consulta(self, paciente, data, dentista):
        consulta = {"paciente": paciente, "data": data, "dentista": dentista}
        self.repo.salvar_consulta(consulta)

    def listar_consultas(self):
        return self.repo.listar_consultas()

    def listar_consultas_paciente(self, nome):
        return [c for c in self.repo.listar_consultas() if c["paciente"] == nome]