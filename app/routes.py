from app import app
from app.controllers.ContactController import contact_controller
from flask import request

# Routes of contact

@app.route('/contacts', methods=['GET', 'POST'])
def contacts_handler():
    if request.method == 'POST':
        return contact_controller.add_contact()
    if request.method == 'GET':
        return contact_controller.get_contacts()

@app.route('/contacts/<contact_id>', methods=['PUT', 'GET', 'DELETE'])
def contact_handler(contact_id):
    if request.method == 'GET':
        return contact_controller.get_contact(contact_id)
    if request.method == 'PUT':
        return contact_controller.update_contact(contact_id)
    if request.method == 'DELETE':
        return contact_controller.delete_contact(contact_id)
