from Exercise1 import ItemBiblioteca 

class Revista(ItemBiblioteca):
    def __init__(self, titulo, ano_publicacao, edicao):
        super().__init__(titulo, ano_publicacao)
        if edicao <= 0:
            raise ValueError("Número da edição deve ser maior que 0.")
        self.edicao = edicao

    def atualizar_edicao(self, nova_edicao):
        if nova_edicao <= 0:
            raise ValueError("Número da nova edição deve ser maior que 0.")
        self.edicao = nova_edicao

    def restringir_emprestimo(self, dias_max):
      
        if self.ano_publicacao < 2000:
            return dias_max <= 7
        return True

    def obter_info(self):
        info_base = super().obter_info()
        return f"{info_base}, Edição: {self.edicao}"
