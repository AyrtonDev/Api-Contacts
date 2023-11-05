from flask import request
from app.models.Contacts import ContactProps
from app.repositories.ContactRepository import ContactRepository
from app.utils import is_valid_uuid, build_reponse, verify_attrb

class ContactController:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def get_contacts(self):
        return build_reponse(
            message="Get list contacts",
            data=self.contact_repository.get_all()
        )

    def get_contact(self, contact_id):
        is_uuid = is_valid_uuid(contact_id)

        if is_uuid is False:
            return build_reponse(
                message="Invalid contact id",
                data=None,
                status=400
            )

        contact = self.contact_repository.get_by_id(contact_id)

        if contact is None:
            return build_reponse(
                message="Contact not found",
                data=None,
                status=500
            )

        if contact == "Contact not found":
            return build_reponse(
                message="Contact not found",
                data=None,
                status=404
            )

        return build_reponse(
            message="Contact found",
            data=contact
        )

    def add_contact(self):
        contact = request.get_json()

        if verify_attrb(contact, 'name'):
            return build_reponse(
                message="Name is required",
                data=None,
                status=400
            )

        if verify_attrb(contact, 'email') or \
            verify_attrb(contact, 'phone'):
            return build_reponse(
                message="E-mail or phone field have to be full",
                data=None,
                status=400
            )

        newContact = self.contact_repository.add(contact)

        if newContact is None:
            return build_reponse(
                message="Internal error",
                data=None,
                status=500
            )

        return build_reponse(
            message="Contact added",
            data={'id': newContact},
            status=201
        )

    def update_contact(self, contact_id):
        contact = request.get_json()

        is_uuid = is_valid_uuid(contact_id)

        if is_uuid is False:
            return build_reponse(
                message="Invalid contact id",
                data=None,
                status=400
            )

        if verify_attrb(contact, 'name'):
            return build_reponse(
                message="Name is required",
                data=None,
                status=400
            )

        if verify_attrb(contact, 'email') or \
            verify_attrb(contact, 'phone'):
            return build_reponse(
                message="E-mail or phone field have to be full",
                data=None,
                status=400
            )

        contact_updated = self.contact_repository.update_by_id(contact_id, contact)

        if contact_updated is None:
            return build_reponse(
                message="Internal error",
                data=None,
                status=500
            )

        if contact_updated == "Contact not found":
            return build_reponse(
                message="Contact not found",
                data=None,
                status=404
            )

        return build_reponse(
                message="Contact was updated",
                data={'id': contact_id }
            )

    def delete_contact(self, contact_id):
        is_uuid = is_valid_uuid(contact_id)

        if is_uuid is False:
            return build_reponse(
                message="Invalid contact id",
                data=None,
                status=400
            )

        contact = self.contact_repository.delete_by_id(contact_id)

        if contact is None:
            return build_reponse(
                message="Internal error",
                data=None,
                status=500
            )

        if contact == "Contact not found":
            return build_reponse(
                message="Contact not found",
                data=None,
                status=404
            )

        return build_reponse(
            message=f"Contact {contact_id} was deleted",
            data=None,
            status=204
        )

contact_controller = ContactController(ContactRepository())
