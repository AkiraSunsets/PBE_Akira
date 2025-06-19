from Exercise1 import ItemBiblioteca 

class ColecaoLivros(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao):
        super().__init__(titulo, ano_publicacao)  
        self.livros = []

    def adicionar_livro(self, livro: ItemBiblioteca):
        self.livros.append(livro)

    def verificar_disponibilidade_colecao(self):
        for livro in self.livros:
            if not livro.disponivel:
                return False
        return True  

    def obter_info(self):
        retorno = super().obter_info()
        for livro in self.livros:
            retorno += f'\n {livro.obter_info()}'
        return retorno
