class Biblioteca:
    def __init__(self):
        self.itens = {}  

    def adicionar_item(self, item):
        if item.titulo in self.itens:
            raise Exception("Já existe um item com este título na biblioteca.")
        self.itens[item.titulo] = item

    def remover_item(self, titulo):
        if titulo not in self.itens:
            raise Exception("Item não encontrado na biblioteca.")
        del self.itens[titulo]

    def listar_itens_disponiveis(self):
        disponiveis = []
        for item in self.itens.values():
            if item.disponivel:
                disponiveis.append(item.titulo)
        return disponiveis

    def contar_itens_emprestados(self):
        contador = 0
        for item in self.itens.values():
            if not item.disponivel:
                contador += 1
        return contador
