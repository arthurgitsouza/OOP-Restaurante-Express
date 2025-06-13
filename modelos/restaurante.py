class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome.tittle()
        self.categoria = categoria
        self._ativo = False   # O _ antes da variavel significa que o programa não vai deixar que o usuário altere o valor dele (O usuário não vai acessar ele diretamente, somente através do metódo @property)
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def list_restaurants():
        for restaurant in Restaurante.restaurantes:
            print(f'{restaurant.nome} | {restaurant.categoria} | {restaurant.ativo}')
     
    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Desativado'
    
restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiano')

Restaurante.list_restaurants()
