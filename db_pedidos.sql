create database db_pedidos;

use db_pedidos;

create table pedido (
    id_pedido int auto_increment primary key,
    cliente varchar(100)
);


create table Item_pedido (
    id int auto_increment primary key,
    id_pedido int,
    produto varchar(100),
    quantidade int,
    preco decimal(10, 2),
    categoria varchar(100),
    foreign key (id_pedido) references (id_pedido)
);