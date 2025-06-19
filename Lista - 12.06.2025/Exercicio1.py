
class ItemBiblioteca:
    def __init__(self, titulo: str, ano_publicacao: int):
        self.titulo = titulo
        self.ano_publicacao = ano_publicacao
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == False:
            raise Exception("Item já emprestado!")
        else:
            self.disponivel = False

    def devolver(self):
        if self.disponivel == True:
            raise Exception("Item já está disponível!")
        else:
            self.disponivel = True

    def obter_info(self):
        if self.disponivel == True:
            esta_disponivel = "Sim"
        else:
            esta_disponivel = "Não"
        string_formada = f"Título: {self.titulo}, Ano: {self.ano_publicacao}, Disponível: {esta_disponivel}"
        return string_formada
