# Responsável por salvar e carregar dados em JSON (persistência simples)

import json
from os.path import exists

class RepositorioJSON:
    def __init__(self, arquivo):
        self.arquivo = arquivo

        # Se o arquivo não existir, cria um vazio
        if not exists(self.arquivo):
            self._salvar({"pacientes": [], "consultas": [], "usuarios": []})

    def _carregar(self):
        # Carrega todo o banco de dados
        with open(self.arquivo, "r", encoding="utf-8") as arq:
            return json.load(arq)

    def _salvar(self, dados):
        # Salva todo o banco de dados
        with open(self.arquivo, "w", encoding="utf-8") as arq:
            json.dump(dados, arq, indent=4, ensure_ascii=False)

    # CRUD simples

    def listar(self, chave):
        return self._carregar()[chave]

    def adicionar(self, chave, objeto):
        dados = self._carregar()
        dados[chave].append(objeto)
        self._salvar(dados)

    def atualizar_lista(self, chave, lista):
        dados = self._carregar()
        dados[chave] = lista
        self._salvar(dados)