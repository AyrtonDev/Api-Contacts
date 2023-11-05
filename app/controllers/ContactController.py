from flask import request
from app.repositories.ContactRepository import ContactRepository
from app.utils import print_error, is_valid_uuid, build_response, verify_attrb

class ContactController:
    def __init__(self, contact_repository: ContactRepository):
        self.contact_repository = contact_repository

    def all(self):
        try:
            return build_response(
                message="Get list contacts",
                data=self.contact_repository.all()
            )

        except Exception as e:
            print_error(e)

    def one(self, contact_id):
        try:
            is_uuid = is_valid_uuid(contact_id)

            if is_uuid is False:
                return build_response(
                    message="Invalid contact id",
                    data=None,
                    status=400
                )

            contact = self.contact_repository.one_by_id(contact_id)

            if contact == "Contact not found":
                return build_response(
                    message="Contact not found",
                    data=None,
                    status=404
                )

            return build_response(
                message="Contact found",
                data=contact
            )

        except Exception as e:
            print_error(e)

    def create(self):
        try:
            contact = request.get_json()

            if verify_attrb(contact, 'name'):
                return build_response(
                    message="Name is required",
                    data=None,
                    status=400
                )

            if verify_attrb(contact, 'email') or \
                verify_attrb(contact, 'phone'):
                return build_response(
                    message="E-mail or phone field have to be full",
                    data=None,
                    status=400
                )

            newContact = self.contact_repository.create(contact)

            return build_response(
                message="Contact added",
                data={'id': newContact},
                status=201
            )

        except Exception as e:
            print_error(e)

    def update(self, contact_id):
        try:
            contact = request.get_json()

            is_uuid = is_valid_uuid(contact_id)

            if is_uuid is False:
                return build_response(
                    message="Invalid contact id",
                    data=None,
                    status=400
                )

            if verify_attrb(contact, 'name'):
                return build_response(
                    message="Name is required",
                    data=None,
                    status=400
                )

            if verify_attrb(contact, 'email') or \
                verify_attrb(contact, 'phone'):
                return build_response(
                    message="E-mail or phone field have to be full",
                    data=None,
                    status=400
                )

            contact_updated = self.contact_repository.update(contact_id, contact)

            if contact_updated == "Contact not found":
                return build_response(
                    message="Contact not found",
                    data=None,
                    status=404
                )

            return build_response(
                    message="Contact was updated",
                    data={'id': contact_id }
                )

        except Exception as e:
            print_error(e)

    def delete(self, contact_id):
        try:
            is_uuid = is_valid_uuid(contact_id)

            if is_uuid is False:
                return build_response(
                    message="Invalid contact id",
                    data=None,
                    status=400
                )

            contact = self.contact_repository.delete(contact_id)

            if contact == "Contact not found":
                return build_response(
                    message="Contact not found",
                    data=None,
                    status=404
                )

            return build_response(
                message=f"Contact {contact_id} was deleted",
                data=None,
                status=204
            )

        except Exception as e:
            print_error(e)

contact_controller = ContactController(ContactRepository())
