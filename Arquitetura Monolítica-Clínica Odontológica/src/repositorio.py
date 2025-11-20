import json
import os

class RepositorioJSON:
    """Responsável por salvar e carregar dados do sistema."""

    def __init__(self, caminho):
        self.caminho = caminho
        self._garantir_arquivo()

    # Garante que o JSON nunca esteja vazio
    def _garantir_arquivo(self):
        if not os.path.exists(self.caminho) or os.path.getsize(self.caminho) == 0:
            with open(self.caminho, "w") as f:
                json.dump({"usuarios": [], "pacientes": [], "consultas": []}, f, indent=4)

    def _carregar(self):
        with open(self.caminho, "r") as f:
            return json.load(f)

    def _salvar(self, dados):
        with open(self.caminho, "w") as f:
            json.dump(dados, f, indent=4)

    # ------------------- USUÁRIOS -------------------
    def listar_usuarios(self):
        return self._carregar()["usuarios"]

    def salvar_usuario(self, usuario):
        dados = self._carregar()
        dados["usuarios"].append(usuario)
        self._salvar(dados)

    # ------------------- PACIENTES -------------------
    def listar_pacientes(self):
        return self._carregar()["pacientes"]

    def salvar_paciente(self, paciente):
        dados = self._carregar()
        dados["pacientes"].append(paciente)
        self._salvar(dados)

    # ------------------- CONSULTAS -------------------
    def salvar_consulta(self, consulta):
        dados = self._carregar()
        dados["consultas"].append(consulta)
        self._salvar(dados)

    def listar_consultas(self):
        return self._carregar()["consultas"]