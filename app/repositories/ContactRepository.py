from app import db
from app.models.Contacts import Contacts

class ContactRepository:
    def all(self):
        try:
            contacts_list = []
            contacts = Contacts.query.all()

            for contact in contacts:
                contacts_list.append({
                    'id': contact.id,
                    'name': contact.name,
                    'email': contact.email,
                    'phone': contact.phone,
                    'category_id': contact.category_id
                })

            return contacts_list
        except Exception as e:
            raise e

    def one_by_id(self, contact_id):
        try:
            contact = Contacts.query.filter_by(id=contact_id).first()

            if contact is None:
                return "Contact not found"

            return {
                    'id': contact.id,
                    'nome': contact.name,
                    'phone': contact.phone,
                    'email': contact.email,
                    'category_id': contact.category_id
                }

        except:
            return None

    def create(self, contact):
        try:
            new_contact = Contacts(
                name=contact['name'],
                email=contact['email'],
                phone=contact['phone'],
                category_id=contact['category_id']
            )

            db.session.add(new_contact)
            db.session.commit()

            return new_contact.id

        except Exception as e:
            raise e

    def update(self, contact_id, contact_data):
        try:
            contact = Contacts.query.filter_by(id=contact_id).first()

            if contact is None:
                return "Contact not found"

            contact.name = contact_data['name']

            if 'email' in contact_data:
                contact.email = contact_data['email']

            if 'phone' in contact_data:
                contact.phone = contact_data['phone']

            if 'category_id' in contact_data:
                contact.category_id = contact_data['category_id']

            db.session.commit()

            return contact_id

        except Exception as e:
            raise e

    def delete(self, contact_id):
        try:
            contact = Contacts.query.filter_by(id=contact_id).first()

            if contact is None:
                return "Contact not found"

            db.session.delete(contact)
            db.session.commit()

            return contact_id

        except Exception as e:
            raise e
