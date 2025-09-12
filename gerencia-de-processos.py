def gerar_pid():
    pid = 0
    while True:
        yield pid
        pid += 1

class Processo():
    def __init__(self, nome: str, tempo_cpu: int, tempo_IO: int, prioridade: str):
        self.pid = gerar_pid()
        self.nome = nome
        self.tempo_cpu = tempo_cpu
        self.tempo_IO = tempo_IO
        self.estado = "Novo"
        self.processos_filhos = []
        self.prioridade = prioridade


class Node():
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class Deque():
    ...


class Escalonador():
    def __init__(self):
        pass