from app import db
from app.models.Contacts import Contacts
from app.models.Contacts import ContactProps

class ContactRepository:
    def add(self, contact):
        new_contact = Contacts(
            name=contact['name'],
            email=contact['email'],
            phone=contact['phone'],
            category_id=contact['categoryId']
        )

        db.session.add(new_contact)
        db.session.commit()

        return new_contact.id

    def get_all(self) -> list[ContactProps] | list :
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

    def get_by_id(self, contact_id) -> ContactProps | None:
        contact = Contacts.query.filter_by(id=contact_id).first()

        if contact:
            return {
                'id': contact.id,
                'name': contact.name,
                'email': contact.email,
                'phone': contact.phone,
                'category_id': contact.category_id
            }
        else:
            return None

    def delete_by_id(self, contact_id):
        return contact_id

    def update_by_id(self, contact_id, contact_data):
        return contact_id

# TODO: finish all repositories
