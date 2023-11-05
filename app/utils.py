import uuid
from flask import make_response, jsonify

def is_valid_uuid(uuid_str:str):
    try:
        uuid_obj = uuid.UUID(uuid_str)
        return str(uuid_obj) == uuid_str  # Verifica se a representação em string é igual à original
    except ValueError:
        return False

def verify_attrb(obj, attrb: str):
    if attrb not in obj:
        return True

    if obj[attrb] is None:
        return True

    if obj[attrb] == "":
        return True

    return False

def build_reponse(data:dict | list | None, message:str, status=200):
    return make_response(
        jsonify(
            message=message,
            data=data
        ),
        status
    )
