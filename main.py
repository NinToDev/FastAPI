from typing import Union
from fastapi import FastAPI
from models.Item import Item
from models.Product import Product


# CREACION DE UN OBJETO DE  LA APLICACION FASTAPI
app = FastAPI()

@app.get('/')
def read_root():
    return {'hello': 'word'}

@app.get('/hello')
def hello_world():
    return {'Hello':'world'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Union[str, None] = None): #q: Union[str, None] = None Puede recibir una cadena o none.
    return {'item_id': item_id, 'q': q}

@app.get('/calculate')
def calculator(op: float, op2: float):
    return {'Sum': op + op2}

@app.put('/item/{item_id}')
def update_item(item_id: int, item: Item):
    return {'item_name': item.name, 'item_id': item_id}

@app.put('/product/{product_id}')
def update_product(product_id: int, product: Product):
    return {'product_id': product_id, 'name': product.name}

