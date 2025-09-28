from models import Pedido, Item_pedido

class pedido_control:
    def __init__(self, db):
        self.db = db

    def salvar_pedido(self, pedido):
        pedido_query = "INSERT INTO pedido (cliente) VALUES (%s)"
        cursor = self.db.execute_query(pedido_query, (pedido.cliente,))
        if cursor:
            pedido.id = cursor.lastrowid
            item_query = "INSERT INTO item_pedido (id_pedido, produto, quantidade, preco, categoria) VALUES (%s, %s, %s, %s, %s)"
            for item in pedido.itens:
                self.db.execute_query(item_query, (pedido.id, item.produto, item.quantidade, item.preco, item.categoria))

    def atualizar_pedido(self, pedido):
        if pedido.id is None:
            raise ValueError("Pedido deve ter um ID para atualizar")
        update_query = "UPDATE pedido SET cliente = %s WHERE id_pedido = %s"
        self.db.execute_query(update_query, (pedido.cliente, pedido.id))

    def deletar_pedido(self, pedido_id):
        deletar_itens = "DELETE FROM item_pedido WHERE id_pedido = %s"
        self.db.execute_query(deletar_itens, (pedido_id,))
        deletar_pedido = "DELETE FROM pedido WHERE id_pedido = %s"
        self.db.execute_query(deletar_pedido, (pedido_id,))

    def listar_pedidos_com_itens(self):
        query = "SELECT p.id_pedido, p.cliente, i.produto, i.quantidade, i.preco, i.categoria FROM pedido p JOIN item_pedido i ON p.id_pedido = i.id_pedido ORDER BY p.id_pedido"
        cursor = self.db.execute_query(query)
        pedidos = {}
        if cursor:
            for id_pedido, cliente, produto, quantidade, preco, categoria in cursor:
                if id_pedido not in pedidos:
                    pedidos[id_pedido] = Pedido(cliente)
                    pedidos[id_pedido].id = id_pedido
                item = Item_pedido(produto, quantidade, preco, categoria)
                pedidos[id_pedido].add_item(item)
        return list(pedidos.values())
