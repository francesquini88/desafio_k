class ProductModel:
    def __init__(self,codigo, preco, nome):
        self.codigo = codigo
        self.preco = preco
        self.nome = nome

    def json(self):
        return {
            'codigo' : self.codigo,
            'nome' : self.nome,
            'preco' : self.preco
        }