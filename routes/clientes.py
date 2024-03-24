from flask import Blueprint, render_template, request
from database.cliente import CLIENTES
from database.models.clientes import Cliente

clientes_routes = Blueprint('clientes', __name__)

@clientes_routes.route('/')
def listar_clientes():
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)

@clientes_routes.route('/', methods=['POST'])
def inserir_clientes():
    data = request.json
    novo_user = Cliente.create(
        nome = data['nome'],
        email = data['email']
    )

    return render_template('item.html', c=novo_user)

@clientes_routes.route('/new')
def form_clientes():
    return render_template('form_cliente.html')

@clientes_routes.route('/<int:cliente_id>/edit')
def form_edit_clientes(cliente_id):
    cliente = Cliente.select().where(Cliente.id == cliente_id).get()
    return render_template('form_cliente.html', cliente = cliente)

@clientes_routes.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_clientes(cliente_id):
    data = request.json
    cliente = Cliente.select().where(Cliente.id == cliente_id).get()
    
    cliente.nome = data['nome']
    cliente.email = data['email']
        
    cliente.save()
    return render_template('item.html', c=cliente)

@clientes_routes.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_clientes(cliente_id):
    cliente = Cliente.select().where(Cliente.id == cliente_id).get()
    cliente.delete_instance()
    return {'deleted':'ok'}