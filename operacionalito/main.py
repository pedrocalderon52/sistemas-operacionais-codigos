from models.processo import Processo

def get_processos():
    with open("operacionalito/dados.txt", "r") as file:
        lines = [line.rstrip() for line in file]
        processos = [] # substituir pela estrutura de dados a ser criada
        for line in lines:
            pid, tempo_entrada, tempo_cpu, tempo_IO, prioridade = line.split(";") # divide as informações da linha com base no ';'
            processos.append(Processo(pid, tempo_entrada, tempo_cpu, tempo_IO, prioridade))
        return processos


print(get_processos())

class Node():
    def __init__(self, valor):
        self.valor = valor
        self.prox = None


class Deque():
    ...

