from database import Database
from models import Pedido, Item_pedido
from control import pedido_control

db = Database(host='127.0.0.1', user='root', password='', database='db_pedidos')

if not db.connection or not db.connection.is_connected():
    print("Conexão com MySQL não estabelecida. Verifique se o serviço está ativo.")
else:
    control = pedido_control(db)

    pedido = Pedido("Claudio Ulisse")
    pedido.add_item(Item_pedido("Notebook", 1, 3500.00, "Eletrônicos"))
    pedido.add_item(Item_pedido("Mouse", 2, 120.00, "Eletrônicos"))
    control.salvar_pedido(pedido)
    print(f"Pedido inserido com id {pedido.id}\n")

    if pedido.id is not None:
        pedido.cliente = "Claudio U."
        control.atualizar_pedido(pedido)
        print("Pedido atualizado\n")

        pedidos = control.listar_pedidos_com_itens()
        for p in pedidos:
            print(f"Pedido {p.id} - Cliente: {p.cliente}")
            for i in p.itens:
                print(f"  Produto: {i.produto}, Quantidade: {i.quantidade}, Preço: {i.preco}, Categoria: {i.categoria}")
        print()

        control.deletar_pedido(pedido.id)
        print(f"Pedido {pedido.id} deletado\n")

    db.close()
