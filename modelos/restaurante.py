from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []    # Lista vazia para armazenar os restaurantes criados

    def __init__(self, nome, categoria):
        self._nome = nome.title()    # Dita qual o nome vai ser dado para o restaurante
        self._categoria = categoria.title()    # Fala qual vai ser a categoria 
        self._ativo = False    # E se vai estar ativo ou não
        self._avaliacao = []    # Cria uma lista vazia paras as notas 
        Restaurante.restaurantes.append(self)    # Adiciona o restaurante criado na lista dentro de Restaurantes

    def __str__(self):
        return f'{self._nome} | {self._categoria}'    # Imprime na tela o nome e categoria do restaurante

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')    #imprime na tela as informações contidas no nome e categoria
        for restaurante in cls.restaurantes:    #Cria um looping conferindo se o restaurante esta dentro da lista Restaurantes
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')    #Printa na tela as informações

    @property
    def ativo(self):    
        return '✓' if self._ativo else '✗'    # Operador ternario para se caso o restaurante estiver ativo vai ser mostrado o "✓" se não "✗"
    
    def alternar_estado(self):
        self._ativo = not self._ativo    # Altera o estado de atividade do restaurante

    def receber_avaliacao(self, cliente, nota):    # Registra avaliações de clientes
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)
    
    @property
    def media_avaliacoes(self):    # Faz toda a media das avaliações
        if not self._avaliacao:
            return 'Ainda sem nota!'    # Se por acaso ainda não houver avaliações ira aparecer "ainda sem nota"
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)    # Operador ternario para percorrer todos os itens da lista ("sum" faz a soma de tudo)
        quantidade_de_notas = len(self._avaliacao)    # "len" pega o valor do tamanho de itens na lista 
        media = soma_das_notas / quantidade_de_notas
        media_final = round(media / 2, 1)    # basicamente pega o valor da media e divide por dois para que a nota seja no maximo 5
        return media_final