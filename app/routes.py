from app import app
from app.controllers.CategoryController import category_controller
from app.controllers.ContactController import contact_controller
from flask import request

# Routes of contact

@app.route('/contacts', methods=['GET', 'POST'])
def contacts_handler():
    if request.method == 'POST':
        return contact_controller.create()
    if request.method == 'GET':
        return contact_controller.all()

@app.route('/contacts/<contact_id>', methods=['PUT', 'GET', 'DELETE'])
def contact_handler(contact_id):
    if request.method == 'GET':
        return contact_controller.one(contact_id)
    if request.method == 'PUT':
        return contact_controller.update(contact_id)
    if request.method == 'DELETE':
        return contact_controller.delete(contact_id)

# Routes of category

@app.route('/categories', methods=['GET', 'POST'])
def categories_handler():
    if request.method == 'POST':
        return category_controller.create()
    if request.method == 'GET':
        return category_controller.all()

@app.route('/categories/<category_id>', methods=['DELETE'])
def category_handler(category_id):
    return category_controller.delete(category_id)
