class Pedido:
    def __init__(self, cliente):
        self.id = None
        self.cliente = cliente
        self.itens = []

    def add_item(self, item):
        self.itens.append(item)


class Item_pedido:
    def __init__(self, produto, quantidade, preco, categoria):
        self.id = None
        self.produto = produto
        self.quantidade = quantidade
        self.preco = preco
        self.categoria = categoria
