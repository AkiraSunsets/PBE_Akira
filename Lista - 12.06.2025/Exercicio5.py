class RelatorioBiblioteca:
    def __init__(self, biblioteca):
        self.biblioteca = biblioteca  

    def gerar_relatorio_completo(self):
        relatorio = "RELATÓRIO COMPLETO:\n"
        for item in self.biblioteca.itens.values():
            relatorio += item.obter_info() + "\n"
        return relatorio

    def gerar_relatorio_disponibilidade(self):
        disponiveis = self.biblioteca.listar_itens_disponiveis()
        total = len(disponiveis)
        relatorio = f"RELATÓRIO DE DISPONIBILIDADE:\nItens disponíveis ({total}):\n"
        relatorio += "\n".join(disponiveis)
        return relatorio

    def gerar_relatorio_emprestimos(self):
        total = len(self.biblioteca.itens)
        emprestados = self.biblioteca.contar_itens_emprestados()
        proporcao = (emprestados / total) * 100 if total > 0 else 0
        return (
            "RELATÓRIO DE EMPRÉSTIMOS:\n"
            f"Itens emprestados: {emprestados}\n"
            f"Proporção emprestada: {proporcao:.2f}%"
        )
